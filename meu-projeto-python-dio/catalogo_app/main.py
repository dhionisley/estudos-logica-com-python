# catalogo_app/main.py

# Começamos com uma lista vazia para armazenar nossos itens (livros, filmes, etc.)
# Usaremos uma lista de dicionários, pois cada item terá várias informações.
catalogo = []

def adicionar_item():
    """Função para adicionar um novo item ao catálogo."""
    print("\n--- Adicionar Novo Item ---")
    titulo = input("Digite o título: ")
    autor = input("Digite o autor/diretor: ")
    ano = input("Digite o ano de lançamento: ")

    # Cria um dicionário para representar o item
    item = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": True # Adicionamos um status padrão
    }

    # Adiciona o dicionário à nossa lista 'catalogo'
    catalogo.append(item)
    print(f"\n✅ Item '{titulo}' foi adicionado com sucesso!")

def listar_itens():
    """Função para listar todos os itens do catálogo."""
    print("\n--- Itens no Catálogo ---")

    # Verifica se a lista está vazia
    if not catalogo:
        print("O catálogo está vazio.")
        return # Encerra a função aqui se não houver itens

    # Itera sobre cada item na lista e imprime suas informações
    for item in catalogo:
        status = "Disponível" if item["disponivel"] else "Indisponível"
        print(f"Título: {item['titulo']} | Autor/Diretor: {item['autor']} | Ano: {item['ano']} | Status: {status}")

def main():
    """Função principal que gerencia o menu e a interação com o usuário."""

    while True:
        print("\n===== Menu do Catálogo =====")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_item()
        elif opcao == '2':
            listar_itens()
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break # Quebra o loop 'while' e encerra o programa
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

# Garante que o programa comece a rodar pela função main()
# Esta é uma boa prática em Python.
if __name__ == "__main__":
    main()