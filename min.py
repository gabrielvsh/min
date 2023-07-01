import random

nome = input('informe seu nome:')
inteiro = int(input('informe um numero inteiro:'))
cc = input('escolha par ou impar')
a = random.randint(1,10  )
print('o numero escolhido pelo computador é',a)
if (inteiro+a%2==0):
    if(cc == 'par'):
        print(nome,'deu par,voçê ganhou')
    else:
        print(nome,'deu par,voçê perdeu')
else:
    if(cc == 'impar'):
        print(nome,'deu impar,voçê ganhou')
    else:
        print(nome,'deu impar,voçê perdeu')
