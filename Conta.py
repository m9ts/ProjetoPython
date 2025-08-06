class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Cliente: ", self._titular, "  | ", "Saldo atual: ", self.saldo)
