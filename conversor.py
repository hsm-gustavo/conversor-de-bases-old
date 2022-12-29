from tkinter import *
import tkinter.messagebox as mbox
from string import ascii_uppercase

def erro_de_valor():
    mbox.showerror(title="Erro",message="Valor(es) Inválido(s)")

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
            resto = numero%base_destino
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

def temp_text_origem(e):
    base_origem.delete(0,"end")

def temp_text_num(e):
    numero.delete(0, "end")

def temp_text_destino(e):
    base_destino.delete(0, "end")

def convert():
    try:
        origem = int( base_origem.get() )
        num = numero.get()
        destino = int( base_destino.get() )
        resultado = qualquer_pra_qualquer(num,destino,origem)

        resultado_texto = Label(text=f"{resultado}",font=("Arial",20,"normal"))
        resultado_texto.pack()

    except ValueError:
        erro_de_valor()

def main():
    global base_origem
    global numero
    global base_destino

    window = Tk()
    width = 300
    height = 350
    window.geometry(f"{width}x{height}")
    window.title(string="Conversor de bases")

    conversor_texto = Label(text="Conversor de Bases",pady=10, font=("Arial",20,"bold"))
    conversor_texto.pack()

    base_origem_texto = Label(text="Base de origem:")
    base_origem_texto.pack(side="top")
    base_origem = Entry(bg="#ffffff",width=10,borderwidth=2)
    base_origem.insert(index=0,string="Ex.: 2")
    base_origem.bind("<FocusIn>", temp_text_origem)
    base_origem.pack(side="top")

    numero_texto = Label(text="Número:")
    numero_texto.pack(side="top")
    numero = Entry(bg="#ffffff",width=10,borderwidth=2)
    numero.insert(index=0,string="Ex.: 1011")
    numero.bind("<FocusIn>", temp_text_num)
    numero.pack(side="top")

    base_destino_texto = Label(text="Base de destino:")
    base_destino_texto.pack(side="top")
    base_destino = Entry(bg="#ffffff",width=10,borderwidth=2)
    base_destino.insert(index=0,string="Ex.: 10")
    base_destino.bind("<FocusIn>", temp_text_destino)
    base_destino.pack(side="top")

    converter = Button(text="Converter",command=convert)
    converter.pack()
    
    window.mainloop()

if __name__=="__main__":
    main()