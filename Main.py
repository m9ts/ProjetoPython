from cliente import Cliente
from conta import Conta

print("Testando o projeto")

c1 = Cliente("Jubileu Gois", "115555-6666")
conta = Conta(c1.nome, 8888, 0)

conta.depositar(200)
conta.saque(50)
conta.extrato()
