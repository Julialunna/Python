import forca
import adivinhacao

def escolhe_jogo():
    print("************************************")
    print("********Escolha o seu jogo!*********")
    print("************************************")

    print("(1) Forca (2) Adivinhação")

    jogo=int(input("Qual o jogo?"))
    if(jogo==1):
        forca.jogo_forca()
    elif(jogo==2):
        adivinhacao.jogo_adivinhacao()

if(__name__=="__main__"):
    escolhe_jogo()