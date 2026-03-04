nome = input("Qual produto que deseja?")
preco = input("Qual o preço? ")
estoque = input("Quantos há em estoque? ")
categoria = input("Qual a categoria do produto? ")

produtos =     {
    "nome": nome,
    "preco": preco,
    "estoque": estoque,
    "categoria": categoria

}

print(produtos["nome"])
print(produtos["preco"])
print(produtos["estoque"])
print(produtos["categoria"])
