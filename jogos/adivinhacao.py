import random
print("************************************")
print("Bem vindo(a) ao jogo de Adivinhação!")
print("************************************")

numero_secreto = random.randrange(1,101)
print(numero_secreto)
total_de_tentativas =3

for rodada in range(1,total_de_tentativas + 1):

    chute_str=input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute=int(chute_str)

    if(chute < 1 or chute>100):
        print("Você deve digitar um número entre 1 e 100")
        continue 

    print("Tentativa {} de {}". format(rodada, total_de_tentativas))

    acertou =chute==numero_secreto
    maior=chute>numero_secreto
    menor=chute<numero_secreto

    if(acertou):
        print("Você acertou ")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")

print("Fim do jogo")