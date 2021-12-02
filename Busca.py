import requests


def main():
    print("--------------------")
    print('--- Consulta CEP ---')
    print("--------------------")
    print()

    cep_input = input("Digite o CEP para a consulta: ")

    if len(cep_input) != 8:
        print("O CEP precisa ter 8 dígitos!")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    cep_body = request.json()

    if "erro" not in cep_body:
        print('==> CEP ENCONTRADO <==')

        print("CEP: {}".format(cep_body['cep']))
        print("Rua: {}".format(cep_body['logradouro']))
        print("Bairro: {}".format(cep_body['bairro']))
        print("Cidade: {}".format(cep_body['localidade']))
        print("Estado: {}".format(cep_body['uf']))

    else:
        print(" CEP {} Inválido! ".format(cep_input))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta?\n1. Sim\n2. Não\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')


if __name__ == '__main__':
    main()
