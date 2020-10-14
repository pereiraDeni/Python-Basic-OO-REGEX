#herança é para fazer polimorfismo e reuso
#se só tiver um motivo pode pensar um pouco melhor e utiliza outra forma,
#só precisa utilizar um méthodo que o que você quer tem. Se ele se comporta como.
#Conceito python datamodel - são esses __geitem__ __len__
#Python Data Model
#Inicialização __init__
#representação __str__, repr__
#Container, sequencia __contains__ __iter__ __len__ __getitem__
#numericos __add__ __sub__ __mul__ __mod__

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporada} - {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    #Jeito pythonico de exibir algo
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self.likes}'

# class Playlist(list): Minha classe dessa maneira está fazendo várias coisas que não se sabe o que é, não é uma boa pratica de código
#     def __init__(self, nome, programas):
#         self.nome = nome (Como a gente não sabe todas as funçoes que estão dentro de list esse não é a melhor forma de fazer
#         super().__init__(programas) #Faz com que a Playlist ganhe os atributos do list e com isso já vira iterável

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas #esse underline diz que não pode ser acessível o programas

    def __getitem__(self, item): #Duck typing, só p
        return self._programas[item] #como meu programas não é mais iterável precisa chamar esse método para que ele vire iterável

    @property #é boa prática criar property
    def listagem(self):
        return self._programas

    def __len__(self): #dessa forma eu não preciso chamar a listagem do playlist, eu acesso direto o playlist
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()

vingadores.dar_likes()

tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamnho do Plaulist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    # print(f' {programa.nome} - {detalhes} - {programa.likes}')
    print(programa)