# Dicionário para armazenar as informações do contato
contato = {}

# Solicitando informações ao usuário
contato["nome"] = input("Digite o nome do contato: ")
contato["telefone"] = input("Digite o número de telefone do contato: ")
contato["email"] = input("Digite o endereço de email do contato: ")

# Mostrando informações do contato
print()
print("Informações do contato: ")
print(f"Nome: {contato["nome"]} ")
print(f"Telefone: {contato["telefone"]} ")
print(f"Email: {contato["email"]} ")