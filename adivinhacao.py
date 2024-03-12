import random

print("###### bem vindo ao jogo de adivinhação!! ######")
max_rand = 10
sorteio = random.randint(0, max_rand)

## CRIAR DIFICULDADES. exemplo:
## FÁCIL - 10 TENTATIVAS
## MÉDIO - 5 TENTATIVAS
## DIFICIL - 3 TENTATIVAS

dificuldades = int(input("Digite a operação desejada:\n 1 - fácil\n 2 - médio\n 3 - dificil"))

if dificuldades == 1 :
    print("voce escolheu fácil")
    max_tentativas = 10  
elif dificuldades == 2 :
    print("médio")
    max_tentativas = 5
elif dificuldades == 3 :
    print("dificil")
    max_tentativas = 3

## enquanto 
tentativa = 1
while(tentativa<=max_tentativas):
    chute = int (input("tentativa {} de {} - digite o seu chute, entre 0 a 10: \n". format(tentativa, max_tentativas)))
    acertou = chute == sorteio
    if (acertou) :
        print("Parabéns, você ganhou")
        break
    elif (chute > sorteio):
        print("o número sorteado é menor")
    elif(chute < sorteio) :
        print("o número sorteado é maior")
        
    tentativa = tentativa + 1

print("#### FIM DO JOGO ####")