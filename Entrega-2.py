def mostrar_menu1():
    print("1 - Cadastro de uma nova matéria")
    print("2 - Cadastro de um novo professor")
    print("3 - Cadastro de um novo aluno")
    print("4 - Mostrar todas as matérias cadastradas")
    print("5 - Mostrar todos os professores cadastrados")
    print("6 - Mostrar todos os alunos cadastrados")
    print("7 - Abrir o menu de turmas")
    print("8 - Sair do programa")


def mostrar_menu2():
    print("1 - Cadastro de uma nova turma")
    print("2 - Designar um professor para uma turma")
    print("3 - Adicionar alunos em uma turma")
    print("4 - Remover alunos de uma turma")
    print("5 - Dar a nota final dos alunos de uma turma")
    print("6 - Mostrar todos os alunos de uma turma (em ordem alfabética)")
    print("7 - Mostrar todas as turmas cadastradas (em ordem decrescente do número de alunos)")
    print("8 - Voltar para o Menu Principal")


def tratamento(valor, comando, n1, n2):
    while True:
        try:
            valor = int(valor)
            if valor < n1 or valor > n2:
                raise ValueError
        except ValueError:
            print(30 * "-")
            print("O valor digitado deve ser um número inteiro entre {} e {}!".format(n1, n2))
            print("Tente novamente.")
            print(30 * "-")
            valor = input(comando)
        else:
            break
    return valor


def mostrar_cadastrados(lista, comando):
    print(30 * "-")
    print(comando)
    for obj in lista:
        print("{}; ".format(obj.nome))
    print(30 * "-")


class Materia:
    def __init__(self):
        self.nome = input("Insira o nome da matéria: ")


class Turma(Materia):
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
    
    def receber_professor(self, nome_professor):
        self.professor = nome_professor


class Professor(Turma):
    turmas = []

    def __init__(self):
        self.nome = input("Insira o nome do professor: ")
    
    def receber_turma(self, nome_turma):
        self.turmas.append(nome_turma)


class Aluno(Turma):
    def __init__(self):
        self.nome = input("Insira o nome do aluno: ")


def main():
    lista_materias = []
    lista_turmas = []
    lista_professores = []
    lista_alunos = []
    while True:
        mostrar_menu1()
        resp = input("Digite a opção desejada: ")
        resp = tratamento(resp, "Digite a opção desejada: ", 1, 8)

        if resp == 1:
            lista_materias.append(Materia())
            print(30 * "-")

        elif resp == 2:
            lista_professores.append(Professor())
            print(30 * "-")

        elif resp == 3:
            lista_alunos.append(Aluno())
            print(30 * "-")

        elif resp == 4:
            mostrar_cadastrados(lista_materias, "As matérias cadastradas são: ")

        elif resp == 5:
            mostrar_cadastrados(lista_professores, "Os professores cadastrados são: ")

        elif resp == 6:
            mostrar_cadastrados(lista_alunos, "Os alunos cadastrados são: ")

        elif resp == 7:
            while True:
                print(30 * "-")
                mostrar_menu2()
                resp = input("Digite a opção desejada: ")
                resp = tratamento(resp, "Digite a opção desejada: ", 1, 8)

                if resp == 1:
                    if len(lista_materias) == 0:
                        print("Nenhuma matéria foi cadastrada por enquanto.")
                        print("Cadastre uma matéria primeiro para poder cadastrar uma turma.")
                        break

                    else:
                        nome = input("Insira o nome da turma: ")
                        mostrar_cadastrados(lista_materias, "As matérias cadastradas são: ")
                        numero = input("Digite um valor entre 1 e {} para identificar a matéria correspondente: ".format(len(lista_materias)))
                        numero = tratamento(numero, "Digite a opção desejada: ", 1, len(lista_materias))
                        lista_turmas.append(Turma(nome, lista_materias[numero - 1].nome))

                elif resp == 2:
                    if len(lista_professores) == 0:
                        print("Nenhum professor foi cadastrado por enquanto.")
                        print("Cadastre um professor primeiro para poder designá-lo a uma turma.")
                        break

                    else:
                        mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                        numero_turma = input("Digite um valor entre 1 e {} para identificar a turma correspondente: ".format(len(lista_turmas)))
                        numero_turma = tratamento(numero_turma, "Digite a opção desejada: ", 1, len(lista_turmas))

                        mostrar_cadastrados(lista_professores, "Os professores cadastrados são: ")
                        numero_professor = input("Digite um valor entre 1 e {} para identificar o professor correspondente: ".format(len(lista_professores)))
                        numero_professor = tratamento(numero_professor, "Digite a opção desejada: ", 1, len(lista_professores))

                        lista_turmas[numero_turma - 1].receber_professor(lista_professores[numero_professor - 1].nome)
                        lista_professores[numero_professor - 1].receber_turma(lista_turmas[numero_turma - 1].nome)

                elif resp == 3:
                    pass

                elif resp == 4:
                    pass

                elif resp == 5:
                    pass

                elif resp == 6:
                    pass

                elif resp == 7:
                    pass

                elif resp == 8:
                    break

        elif resp == 8:
            break


main()
