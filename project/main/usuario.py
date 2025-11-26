import getpass

def cria_usuario():
    """
    nome: pede nome do usuário para cadastrar
    senha: senha para cadastrar e posteriormente fazer o login
    nivel: nível do usuário para acessar o sistema
    """
    nome = input("Nome de usuário:    ").lower()
    senha = getpass.getpass("Senha:   ")
    """
    mínimo 8 caracteres
    letra maiúscula
    letra minúscula
    número
    símbolo especial
    """
    nivel = input("Nível de acesso:  ").lower()
    usuario = {
        "nome":nome,
        "senha":senha,
        "nivel":nivel
    }
    return usuario