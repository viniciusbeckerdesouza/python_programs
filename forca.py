print('*************************************************')
print('***Bem	vindo	ao	jogo	da	Forca!***')
print('*************************************************')

palavra_secreta = 'banana'
letras_certas = ['_','_','_','_','_','_']

acertou = False
enforcou = False
erros = 0

while(not acertou and not enforcou):
    chute = input('Escreva uma letra: ')

    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_certas[posicao]	=	letra
        posicao += 1
        else:
            erros+= 1
        
        enforcou = erros ==	6
        acertou	= '_' not in letras_acertadas												
		print(letras_acertadas)



    print(letras_certas)
