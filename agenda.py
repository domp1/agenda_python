import os
from time import sleep
agenda=[]
sair=False
while (sair==False):
  os.system('cls')
  op=int(input("----------- AGENDA -------------\n1 - Para inserir um novo contato\n2 - Exibir a lista de contatos\n3 - Editar um contato\n4 - Remover um contato\n"))

  if(op==1):
    n_cnt=[]
    nome=input("Insira o nome que deseja dar ao contato: ")
    n_cnt.append(nome)
    tel=input("Insira o número de telefone: ")
    n_cnt.append(tel)
    agenda.append(n_cnt)
    os.system('cls')

  if(op==2):
    os.system('cls')
    print("------------- AGENDA -------------")
    for cnt in agenda:
      print("Nome: ",cnt[0],"    Telefone: ",cnt[1])
    sleep(4)

  if(op==3):
    os.system('cls')
    nome=input("Digite o nome do contato que deseja editar: ")
    for i in range(len(agenda)):
      if(agenda[i][0]==nome):
        agenda[i][0]=input("Insira o novo nome do contato: ")
        agenda[i][1]=input("Insira o novo telefone do contato: ")
        os.system('cls')
        break

  if(op==4):
    os.system('cls')
    nome=input("Insira o nome do contato que deseja excluir: ")
    for i in range(len(agenda)):
      if(agenda[i][0]==nome):
        agenda.pop(i)
        os.system('cls')
        break

  elif(op==0):
    sair=True
  