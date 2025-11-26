#Gerenciador de usuários

# Funcionalidades:

# 1 - Cadastra usuário
    # Nome do usuário
    # Senha
    # Nível de acesso (ex.: “admin”, “usuario”)

# 2 - Lista usuários
    # Mostrar todos os usuários cadastrados com nível de acesso

# 3 - Busca usuário
    # Consultar se um usuário existe

# 4 - Remove usuário
    # Permite remover usuário pelo nome

# 5 - Sai do sistema


from usuario import cria_usuario #>>>>> em outro arquivo criei uma função que cadastra os usuários, então só precisei importar essa função aqui.
#Isso serve para diminuir o programa principal

usuarios = [] #>>>>> todos os usuários serão armazenados em uma lista. Contém um dicionário com nome, senha e nível.
opcao = 0 

while opcao != 5: #>>>>> loop principal do menu

    print("\n[1] - CADASTRAR USUÁRIO ")
    print("[2] - LISTAR USUÁRIOS")
    print("[3] - BUSCAR USUÁRIO")
    print("[4] - REMOVER USUÁRIO")
    print("[5] - SAIR")

    try:
        opcao = int(input("Digite a opção desejada:     "))
        print()
    except ValueError: # >>>>> toda vez que alguém digitar uma letra ou outro caractere vai dar ValueError e fechar o programa. Este except resolve isso
        print("Digite apenas o número da opção desejada")
        continue

    if opcao == 1:
        novo_usuario = cria_usuario() 
        if any(u["nome"] == novo_usuario["nome"] for u in usuarios): #>>>>> verifica se há algum cadastro com o mesmo nome
            print("\nUsuário já cadastrado!")
        else:
            usuarios.append(novo_usuario) 
            print("\nUsuário cadastrado com sucesso!")

    elif opcao == 2:
        if not usuarios: #>>>>> verifica se a lista está vazia
            print("Sem usuários cadastrados!")
        else:
            print("--LISTA DE USUÁRIOS--")
            for usuario in usuarios:
                print(f"\nUsuário: {usuario['nome']}")
                print(f"Nível de acesso: {usuario['nivel']}")
        
    elif opcao == 3:
        buscar = input("Digite um usuário para buscar:  ").lower()
        encontrado = False #>>>>> Variável de controle que indica se o usuário foi encontrado durante a iteração
        for usuario in usuarios:
            if usuario["nome"].lower() == buscar.lower():
                print("\nUsuário encontrado")
                print(f"\nUsuário: {usuario['nome']}")
                print(f"Nível de acesso: {usuario['nivel']}")
                encontrado = True
                break 
        if not encontrado:
            print("\n Usuário não encontrado")
    
    elif opcao == 4:
        print("--LISTA DE USUÁRIOS CADASTRADOS--")
        for usuario in usuarios:
            print(f"\nUsuário: {usuario['nome']}")
            print(f"Nível de acesso: {usuario['nivel']}")
        remover = input("\nDigite o usuário que deseja remover:    ").lower()
        removido = False #>>>>> variável de controle para remover o usuário
        for usuario in usuarios:
            if usuario["nome"] == remover:
                removido = True
                usuarios.remove(usuario)
                print("\nUsuário removido com sucesso!")
                break

        if not removido:
            print("\nUsuário não encontrado")




                