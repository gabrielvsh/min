e = int(input('quantos elefantes voçê escolhe para a canção:'))
for x in range (0,e):
    if(x == 1):
        print(x,'elefante incomoda muito gente')
    elif (x%2==0):
        t = 'incomodam '*x
        print(x,'elefantes',t,'muito mais')
    else:
        print(x,'elefantes incomodam muita gente')
