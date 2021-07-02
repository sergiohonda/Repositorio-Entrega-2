import copy


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


def tratamento_objetos(lista, nome):
    for obj in lista:
        if obj.nome == nome:
            return 0
    return 1


def mostrar_cadastrados(lista, comando):
    print(30 * "-")
    print(comando)
    for obj in lista:
        print("{}; ".format(obj.nome))
    print(30 * "-")


def mostrar_lista_normal(lista, comando):
    print(30 * "-")
    print(comando)
    for i in range(len(lista)):
        print("{}; ".format(lista[i]))
    print(30 * "-")


def perguntar_numero(lista, nome):
    numero_resultante = input("Digite um valor entre 1 e {} para identificar o(a) {} correspondente: ".format(len(lista), nome))
    numero_resultante = tratamento(numero_resultante, "Digite a opção desejada: ", 1, len(lista))
    return numero_resultante


def procurar_nome(lista, nome):
    for i in range(len(lista)):
        if lista[i].nome == nome:
            return i


def listar_turmas(lista):
    lista_auxiliar = copy.deepcopy(lista)
    numero_alunos_turma = []
    for i in range(len(lista_auxiliar)):
        numero_alunos_turma.append(len(lista_auxiliar[i].alunos))
    numero_turmas = len(lista_auxiliar)
    while numero_turmas != 0:
        indice_auxiliar = 0
        for i in range(len(numero_alunos_turma)):
            if numero_alunos_turma[i] > numero_alunos_turma[indice_auxiliar]:
                indice_auxiliar = i
        print("Turma: {}; Alunos inscritos: {}".format(lista_auxiliar[indice_auxiliar].nome, len(lista_auxiliar[indice_auxiliar].alunos)))
        numero_turmas -= 1
        lista_auxiliar.pop(indice_auxiliar)


class Materia:
    def __init__(self, nome):
        self.nome = nome


class Turma(Materia):
    alunos = []
    notas = {}

    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
    
    def receber_professor(self, nome_professor):
        self.professor = nome_professor

    def receber_aluno(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def dar_notas(self):
        for indice in range(len(self.alunos)):
            self.notas[self.alunos[indice]] = input("Digite a nota do(a) aluno(a) {}: ".format(self.alunos[indice]))

    def mostrar_alunos(self):
        alunos_aux = copy.deepcopy(self.alunos)
        sorted(alunos_aux)
        print("Os alunos da turma {}, em ordem alfabética são: ".format(self.nome))
        for i in range(len(alunos_aux)):
            print("{}; ".format(alunos_aux[i]))


class Professor(Turma):
    turmas = []

    def __init__(self, nome):
        self.nome = nome

    def receber_turma(self, nome_turma):
        self.turmas.append(nome_turma)


class Aluno(Turma):
    turmas = []

    def __init__(self, nome):
        self.nome = nome
    
    def receber_turma(self, nome_turma):
        self.turmas.append(nome_turma)

    def remover_turma(self, nome_turma):
        for i in range(len(self.turmas)):
            if self.turmas[i] == nome_turma:
                self.turmas.pop(i)


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
            nome = input("Insira o nome da matéria: ")
            if tratamento_objetos(lista_materias, nome) == 0:
                print("A matéria inserida já está cadastrada.")
                print(30 * "-")
            else:
                lista_materias.append(Materia(nome))
                print(30 * "-")

        elif resp == 2:
            nome = input("Insira o nome do professor: ")
            if tratamento_objetos(lista_professores, nome) == 0:
                print("O professor inserido ja esta cadastrado.")
                print(30 * "-")
            else:
                lista_professores.append(Professor(nome))
                print(30 * "-")

        elif resp == 3:
            nome = input("Insira o nome do aluno: ")
            if tratamento_objetos(lista_alunos, nome) == 0:
                print("O aluno inserido já está cadastrado.")
                print(30 * "-")
            else:
                lista_alunos.append(Aluno(nome))
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
                        numero = perguntar_numero(lista_materias, "matéria")
                        lista_turmas.append(Turma(nome, lista_materias[numero - 1].nome))

                elif resp == 2:
                    if len(lista_professores) == 0:
                        print("Nenhum professor foi cadastrado por enquanto.")
                        print("Cadastre um professor primeiro para poder designá-lo a uma turma.")
                        break

                    elif len(lista_turmas) == 0:
                        print("Nenhuma turma foi cadastrada por enquanto.")
                        print("Cadastre uma turma primeiro para poder designar um professor a ela.")
                        break

                    else:
                        mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                        numero_turma = perguntar_numero(lista_turmas, "turma")
                        mostrar_cadastrados(lista_professores, "Os professores cadastrados são: ")
                        numero_professor = perguntar_numero(lista_professores, "professor")

                        lista_turmas[numero_turma - 1].receber_professor(lista_professores[numero_professor - 1].nome)
                        lista_professores[numero_professor - 1].receber_turma(lista_turmas[numero_turma - 1].nome)

                elif resp == 3:
                    if len(lista_alunos) == 0:
                        print("Nenhum aluno foi cadastrado por enquanto.")
                        print("Cadastre um aluno primeiro para poder designá-lo a uma turma.")
                        break

                    elif len(lista_turmas) == 0:
                        print("Nenhuma turma foi cadastrada por enquanto.")
                        print("Cadastre uma turma primeiro para poder designar um professor a ela.")
                        break

                    else:
                        mostrar_cadastrados(lista_alunos, "Os alunos cadastrados são: ")
                        numero_aluno = perguntar_numero(lista_alunos, "aluno")
                        mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                        numero_turma = perguntar_numero(lista_turmas, "turma")

                        lista_turmas[numero_turma - 1].receber_aluno(lista_alunos[numero_aluno - 1].nome)

                elif resp == 4:
                    if len(lista_alunos) == 0:
                        print("Nenhum aluno foi cadastrado por enquanto.")
                        print("Cadastre um aluno primeiro para poder designá-lo a uma turma.")
                        break

                    elif len(lista_turmas) == 0:
                        print("Nenhuma turma foi cadastrada por enquanto.")
                        print("Cadastre uma turma primeiro para poder designar um professor a ela.")
                        break

                    else:
                        mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                        numero_turma = perguntar_numero(lista_turmas, "turma")
                        mostrar_lista_normal(lista_turmas[numero_turma - 1].alunos, "Os alunos cadastrados nessa turma são: ")
                        numero_aluno = perguntar_numero(lista_alunos, "aluno")

                        lista_turmas[numero_turma - 1].alunos.pop(numero_aluno - 1)

                elif resp == 5:
                    mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                    numero_turma = perguntar_numero(lista_turmas, "turma")
                    lista_turmas[numero_turma - 1].dar_notas()

                elif resp == 6:
                    mostrar_cadastrados(lista_turmas, "As turmas cadastradas são: ")
                    numero_turma = perguntar_numero(lista_turmas, "turma")
                    lista_turmas[numero_turma - 1].mostrar_alunos()

                elif resp == 7:
                    listar_turmas(lista_turmas)

                elif resp == 8:
                    break

        elif resp == 8:
            break


main()
