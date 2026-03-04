lista_produtos =[]

while True: 

    nome = input("Qual produto que deseja?")
    preco = float(input("Qual o preço? "))
    estoque = input("Quantos há em estoque? ")
    categoria = input("Qual a categoria do produto? ")

    produtos =     {
     "nome": nome,
     "preco": preco,
     "estoque": estoque,
     "categoria": categoria

    }

    lista_produtos.append(produtos)

    print(produtos["nome"])
    print(produtos["preco"])
    print(produtos["estoque"])
    print(produtos["categoria"])

    pergunta = input("Você deseja adicionar mais produtos? Digite S ou N: ").upper()

    if pergunta != "S":
        print("Encerrando o cadastro...")
        print(lista_produtos)
        break
