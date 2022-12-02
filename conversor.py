from string import ascii_uppercase

#convertendo letras para numeros
def converter_letras(num):
    alfabeto = list(ascii_uppercase)
    lista_num = [num for num in range(10,37)]
    return lista_num[alfabeto.index(num)]
#convertendo numeros para letras
def converter_numeros(num):
    alfabeto = list(ascii_uppercase)
    lista_num = [num for num in range(10,37)]
    return alfabeto[lista_num.index(num)]

def qualquer_para_decimal(numero,base_origem):

    soma1=0
    soma2=0
    #troca virgula por ponto se tiver
    numero = numero.replace(",",".")
    #separa a parte inteira da decimal
    if "." in numero:
        inteiro,decimal = str(numero).split(".")
        for index,num in enumerate(inteiro[::-1]):
            if num.isalpha():
                num = converter_letras(num)
            num=int(num)
            soma1+=num*(base_origem**index)
        for index,num in enumerate(decimal):
            if num.isalpha():
                num = converter_letras(num)
            num=int(num)
            soma2+=num*(base_origem**(-(index+1)))
    else:
        for index,num in enumerate(numero[::-1]):
            if num.isalpha():
                num = converter_letras(num)
            num=int(num)
            soma1+=num*(base_origem**index)
    
    #itera pelos numeros e indice dos numeros
    
    resultado_inteiro = soma1 + soma2
    return resultado_inteiro

#convertendo decimal para qualquer base
def decimal_para_qualquer(numero,base_destino):
    #se tiver virgula troca pra ponto 
    numero = numero.replace(",",".")
    if base_destino==10:
        return numero
    #se for decimal
    if "." in numero:
        #separa a parte decimal da parte inteira
        inteiro,decimal = numero.split(".")
        primeiro = str()
        segundo = str()
        
        inteiro = int(inteiro)
        decimal = "0."+decimal
        decimal = float(decimal)

        while inteiro>=1:
            resto = inteiro%base_destino
            if resto>=10:
                resto = converter_numeros(resto)
            primeiro+=str(resto)
            inteiro //= base_destino
        
        digitos = 0
        
        while decimal>0 and digitos<10:
            decimal*=base_destino
            num = int(decimal)
            if num>=10:
                segundo+=converter_numeros(num)
            else:
                segundo+=str(int(decimal))
            decimal-=int(decimal)
            digitos+=1
        
        resultado=primeiro[::-1]+"."+segundo
        
        return resultado 


    else:
        numero = int(numero)
        resultado = str()

        while numero>=1:
            resto = numero%2
            if resto>=10:
                resto = converter_numeros(resto)
            resultado+=str(resto)
            numero //= base_destino

        return resultado[::-1]
          
    
def qualquer_pra_qualquer(numero,base_destino,base_origem):
    if base_destino==10:
        return qualquer_para_decimal(numero,base_origem)
    elif base_origem==10:
        return decimal_para_qualquer(numero,base_destino)
    else:
        if base_origem==base_destino:
            numero = numero.replace(",",".")
            return numero
        num = qualquer_para_decimal(numero,base_origem)
        return decimal_para_qualquer(num,base_destino)
    
    

def main():
    base_origem = int(input("Base de origem: "))
    numero = input("Número a ser convertido: ")
    base_destino = int(input("Base de destino: "))
    resultado= qualquer_pra_qualquer(numero,base_destino,base_origem)

    print(f"Resultado: {resultado}")    

if __name__=="__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nSaindo do aplicativo...")