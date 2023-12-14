class Tarefa:
    id = None
    nome= None
    descricao = None
    tempo= None
    status= None

lista_tarefas=[]

def menu_principal(): 
    while True:
        print("---------------------------------------")
        print(" % SISTEMA DE GERENCIAMENTO DE TAREFAS % ")
        print("---------------------------------------")
        print("\t __________________")
        print(" \t|  Menu Principal  |")
        print("---------------------------------------")
        print("\tDigite a opção desejada:")
        print("\t(1) Adicionar tarefa")
        print("\t(2) Visualizar tarefas")
        print("\t(0) Sair")
        opcao = int(input("Digite a opção:"))
        if opcao == 0:
            break
        elif opcao == 1:
            adiciona_tarefa()
            break
        elif opcao == 2:
            menu_visualizacao()
            break
        while opcao not in [0, 1, 2]:
            opcao = int(input("Opção inválida. Digite novamente:"))   
            if opcao == 0:
                break
            elif opcao == 1:
                adiciona_tarefa()
                break
            elif opcao == 2:
                menu_visualizacao()
                break

def adiciona_tarefa(): 
    new=Tarefa()
    new.nome= input("Digite o nome da tarefa: ") 
    new.id = int(input("Digite um número para ser o identificador da tarefa: "))
    new.descricao= input("Digite a descrição da tarefa: ")
    new.tempo = int(input("Digite um número para o tempo de realização da tarefa, em horas: "))
    new.status= "ATIVA"
    id_igual=False
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].id == new.id:
            print("Já existe uma tarefa com este ID. Por favor, tente novamente.")
            id_igual=True
            adiciona_tarefa()
            break
    if not id_igual:
        lista_tarefas.append(new)
        while True:
            print("\n***Tarefa adicionada. Você pode consultá-la no menu de visualização, em (2)Visualizar tarefas***")
            print("\t(1) Adicionar outra tarefa")
            print("\t(2) Visualizar tarefas")
            print("\t(0) Sair")
            opcao = int(input("Digite a opção:"))
            if opcao == 0:
                break
            elif opcao == 1:
                adiciona_tarefa()
                break
            elif opcao == 2:
                menu_visualizacao()
                break
            while opcao not in [0, 1, 2]:
                opcao = int(input("Opção inválida. Digite novamente:"))
                if opcao == 0:
                    break
                elif opcao == 1:
                    adiciona_tarefa()
                    break
                elif opcao == 2:
                    menu_visualizacao()
                    break

def menu_visualizacao(): 
    print("---------------------------------------")
    print(" % SISTEMA DE GERENCIAMENTO DE TAREFAS %")
    print("---------------------------------------")
    print("\t ________________________")
    print(" \t|  Menu de Visualização  |")       
    for i in range(len(lista_tarefas)):
        print("---------------------------------------------------------------------------------------------------------------------") 
        print(f"|{lista_tarefas[i].id}| {lista_tarefas[i].nome}: {lista_tarefas[i].descricao}.      Tempo estimado:{lista_tarefas[i].tempo}     Status:{lista_tarefas[i].status}") 
    print("---------------------------------------------------------------------------------------------------------------------") 
    print("\t(1) Mudar visualização")
    print("\t(2) Atualizar tarefas")
    print("\t(0) Voltar")
    opcao = int(input("Digite a opção:"))
    if opcao == 0: 
        menu_principal()
    elif opcao == 1: 
        mudar_visualizacao()
    elif opcao == 2:
        atualiza_tarefas()
    while opcao not in [0,1,2]:
        print("Opção inválida.")
        menu_principal()

def mudar_visualizacao():
    print("\n(1) Visualização de tarefas ativas")
    print("(2) Visualização de tarefas concluídas")
    print("(0) Voltar")
    opcao=int(input("Selecione a opção:"))
    if opcao==1:
        visualizacao_ativas()
    elif opcao==2:
        visualizacao_concluidas()
    elif opcao==0:
        menu_visualizacao()
    while opcao not in [0,1,2]:
        print("Opção inválida.")
        menu_principal()

def visualizacao_ativas():
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].status=="ATIVA":
            print("---------------------------------------------------------------------------------------------------------------------") 
            print(f"|{lista_tarefas[i].id}| {lista_tarefas[i].nome}: {lista_tarefas[i].descricao}.      Tempo estimado:{lista_tarefas[i].tempo}     Status:{lista_tarefas[i].status}")
    print("---------------------------------------------------------------------------------------------------------------------") 
    opcao=int(input("pressione 0 para voltar\n"))
    while opcao!=0:
        opcao=int(input())
    mudar_visualizacao()

def visualizacao_concluidas():
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].status=="CONCLUÍDA":
            print("---------------------------------------------------------------------------------------------------------------------") 
            print(f"|{lista_tarefas[i].id}| {lista_tarefas[i].nome}: {lista_tarefas[i].descricao}.      Tempo estimado:{lista_tarefas[i].tempo}     Status:{lista_tarefas[i].status}")
    print("---------------------------------------------------------------------------------------------------------------------") 
    opcao=int(input("pressione 0 para voltar.\n"))
    while opcao!=0:
        opcao=int(input())
    mudar_visualizacao()

def atualiza_tarefas():
    id_encontrado=False
    id=int(input("Digite o ID da tarefa:"))
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].id==id:
            print("---------------------------------------------------------------------------------------------------------------------") 
            print(f"|{lista_tarefas[i].id}| {lista_tarefas[i].nome}: {lista_tarefas[i].descricao}.      Tempo estimado:{lista_tarefas[i].tempo}     Status:{lista_tarefas[i].status}")
            print("---------------------------------------------------------------------------------------------------------------------") 
            id_encontrado=True
            print("(1) Mudar nome")
            print("(2) Mudar descrição")
            print("(3) Mudar tempo estimado")
            print("(4) Marcar como concluída")
            print("(5) Excluir")
            print("(0) Voltar")
            opcao = int(input("Digite a opção:"))
            if opcao == 0:
                menu_visualizacao()
            elif opcao == 1:
                lista_tarefas[i].nome=input("Digite um novo nome para a tarefa:")
                print("***Nome mudado com sucesso.***")
                print("(0)Voltar")
                opcao = int(input())
                if opcao==0:
                    menu_visualizacao()
                while opcao not in [0]:
                    print("Opção inválida.")
                    menu_principal()
            elif opcao == 2:
                lista_tarefas[i].descricao=input("Digite uma nova descrição para a tarefa:")
                print("***Descrição mudada com sucesso.***")
                print("(0)Voltar")
                opcao = int(input())
                if opcao==0:
                    menu_visualizacao()
                while opcao not in [0]:
                    print("Opção inválida.")
                    menu_principal()
            elif opcao == 3:
                lista_tarefas[i].tempo=int(input("Digite um novo tempo para a tarefa:"))
                print("***Tempo mudado com sucesso.***")
                print("(0)Voltar")
                opcao = int(input())
                if opcao==0:
                    menu_visualizacao()
                while opcao not in [0]:
                    print("Opção inválida.")
                    menu_principal()
            elif opcao == 4:
                lista_tarefas[i].status="CONCLUÍDA"
                print("***Status mudado com sucesso.***")
                print("(0)Voltar")
                opcao = int(input())
                if opcao==0:
                    menu_visualizacao()
                while opcao not in [0]:
                    print("Opção inválida.")
                    menu_principal()
            elif opcao == 5:
                lista_tarefas.pop(i)
                print("***Tarefa excluída com sucesso.")
                print("(0)Voltar")
                opcao = int(input())
                if opcao==0:
                    menu_visualizacao()
                while opcao not in [0]:
                    print("Opção inválida.")
                    menu_principal()
            while opcao not in [0, 1, 2, 3, 4, 5]:
                print("Opção inválida.")
                menu_visualizacao()
            break
    if not id_encontrado:
        print("Não há nenhuma tarefa com este id.")
        print("(1)Testar outro ID")
        print("(0)Voltar")
        opcao=int(input("Digite a opção:"))
        if opcao == 1:
            atualiza_tarefas()          
        elif opcao == 0:
            menu_visualizacao()
        while opcao not in [0, 1]:
            opcao = int(input("Opção inválida. Digite novamente:"))
            if opcao == 0:
                menu_visualizacao()
            elif opcao == 1:
                atualiza_tarefas()

menu_principal()