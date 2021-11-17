from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('======================')
    print('==== Bem-Vindo(a) ====')
    print('======================')

    print('''Selecione uma opção abaixo: 
1 - Cadastrar produtos
2 - Listar produtos
3 - Comprar produtos
4 - Visualizar carrinho
5 - Fechar pedido
6 - Sair do sistema''')

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Voltei sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('===================')

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos:')
        print('=====================')

        for produto in produtos:
            print(produto)
            print('=====================')

    else:
        print('Não existem produtos cadastrados!')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja comprar: ')
        print('================================================')
        print('Lista de produtos:')
        for produto in produtos:
            print(produto)
            print('------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'Produto {produto.nome} possiu {quantidade + 1} itens no carrinho!')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'Produto {produto.nome} adicionado no carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi econtrado')
            sleep(2)
            menu()

    else:
        print('Não existem produtos cadastrados!')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('------------------------------')
                sleep(1)
    else:
        print('Carrinho está vazio!')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('================================')
                sleep(1)
        print(f'Valor da compra: {formata_float_str_moeda(valor_total)}')
        print(f'Volte sempre!')
        carrinho.clear()
        sleep(3)

    else:
        print('Carrinho está vazio!')
    sleep(2)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
