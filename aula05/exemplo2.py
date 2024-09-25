import os



os.system('cls')

# turno = int(input('Informe o numero do turno: '))


# match turno:
#     case 1:
#         print('Manhã')
#     case 2:
#         print('Tarde')
#     case 3: 
#         print('Noite')
#     case _:
#         print('Turno inválido')

# mes = int(input('Digite um numero entre 1 e 12:'))


# match mes:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case 4:
#         print('Abril')
#     case 5:
#         print('Maio')
#     case 6:
#         print('Junho')

# print('Escolha um restaurante: \n[1]Chines \n[2]Italiano \n[3]Mexicano \n[4]Vegetariano ')
# res = int(input('Escolha uma opção: '))

# match res:
#     case 1:
#         print('Chinês')
#     case 2:
#         print('Italiano')
#     case 3:
#         print('Mexicano')
#     case 4:
#         print('Vegetariano')
#     case _:
#         print('Opção inválida')

valor = int(input('Insira um numero: '))
print(' [1] Adicionar \n [2]Remover \n [3]listar \n [4]Sair')
opcao = int(input('Selecione uma opção: '))
match opcao:
    case 1:
        # print(f' Adicionar item')
        valor = valor + 1
        print(valor)
    case 2:
        # print(f' Remover item.')
        valor = valor - 1
        print(valor)
    case 3:
        # print(f' Listar item')
        valor
    case 4:
        print(f'Sair')
    case _:
        print('Opção inválida')
