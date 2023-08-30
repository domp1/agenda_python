agenda=[]
sair=False
while (sair==False):
  op=int(input("----------- AGENDA -------------\n\n1 - Para inserir um novo contato\n2 - Exibir a lista de contatos\n3 - Editar um contato\n4 - Remover um contato\n"))

if(op==1):
    n_cnt=[]
    nome=input("Insira o nome que deseja dar ao contato: ")
    n_cnt.append(nome)
    tel=input("Insira o número de telefone")
    n_cnt.append(tel)
    agenda.append(n_cnt)
elif(op==0):
    sair=True
            
  print(agenda)
