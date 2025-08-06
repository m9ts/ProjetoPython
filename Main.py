class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Teodoro", "11111-22222")
conta = Conta(c1.nome, 10101, 0)
print("Nome do titular da conta: ", conta.titular, " | Número da conta: ", conta.numero, " | Saldo: ", conta.saldo)

# Imprime o ID do objeto
print(c1)

# Imprime o conteúdo adicionado
print("Nome: ", c1.nome, " | ", "Telefone:", c1.telefone)


