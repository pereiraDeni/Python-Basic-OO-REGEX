#S - Single responsibility principle
#O - Open/closed principle
#L - Liskov substitution principle
#I - Interface segregation principle
#D - Dependency inversion principle


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f"A conta do {self.__titular} tem extrato de {self.__saldo}")

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def retirar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"A conta do {self.__titular} tem extrato de {self.__saldo}")
        else:
            print("Não pode sacar!")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"A conta do {self.__titular} tem extrato de {self.__saldo}")

    def transferir(self, valor, destino):
        self.retirar(valor)
        destino.depositar(valor)

#Getter and setter

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}