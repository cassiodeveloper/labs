import os

from math import log
patterns =  [        
        (900,	"novecentos"),	(800,	"oitocentos"),
        (700,	"setecentos"),	(600,	"seiscentos"),
        (500,	"quinhentos"),	(400,	"quatrocentos"),
        (300,	"trezentos"),	(200,	"duzentos"),
        (100,	"cento"),	(90,	"noventa"),
        (80,	"oitenta"),	(70,	"setenta"),
        (60,	"sessenta"),	(50,	"cinquenta"),
        (40,	"quarenta"),	(30,	"trinta"),
        (20,	"vinte"),	(19,	"dezenove"),
        (18,	"dezoito"),	(17,	"dezessete"),
        (16,	"dezesseis"),	(15,	"quinze"),
        (14,	"quatorze"),	(13,	"treze"),
        (12,	"doze"),	(11,	"onze"),
        (10,	"dez"),		(9,	"nove"),
        (8,	"oito"),	(7,	"sete"),
        (6,	"seis"),	(5,	"cinco"),
        (4,     "quatro"),	(3,	"três"),
        (2,	"dois"),	(1,	"um") ]

units = ([4, "mil", "mil"],[6,"milhão","milhões"],[9,"trilhão","trilhões"] )



def getScienticNotation(number):        
    power =  (int)(log(number) / log(10));
    fraction = (number / pow(10,power))
    print("notation {0} is  {1} * (10^{2}) ".format(number,fraction,power) )


def between(value, bet1, bet2):
     return bool((bet1 < value) and (value < bet2));


def num2word(number):    
    strAux = ""
    aux = False        
    if number < 1000:
        strAux = write999(number)
    else:
        power =  (int)(log(number) / log(10));
        index = power - 2
        if between(power, 2,6) : # trata de 1001 até 999999
            value = int(str(number)[0: index])            
            restValue = int(str(number)[index: len(str(number))])            
            strAux = write999(value) + " mil "
            if restValue  <=99 :
               strAux +=  "e " + write999(restValue)
            else:
                strAux += write999(restValue)
           
    print(strAux)
        
def write999(number):
    strAux = ""
    divRest = ""
    while True:    
        if number <= 20:            
            strAux = searchPattern(number);
            break
            
        if strAux == "" and  divRest == "":                                    
            strAux =  searchPattern(number)
            divRest = int(number % getRoundedNumber(number))            
            aux =  True
            if divRest == 0:
                break
        else:            
            if aux == False:
                divRest = int(divRest % getRoundedNumber(divRest))
                if divRest == 0:
                    break
            else:
                divRest = divRest
                        
            strAux += " e " + searchPattern(divRest)
            aux = False

    
    return strAux        


def searchPattern(number):    
    for item in patterns:
        value = item[0]
        if value == getRoundedNumber(number):            
            return str(item[1])


def getRoundedNumber(number):
    strNum = ""
    if number > 19:        
        for num in iter(str(number)):            
            if strNum == "":                
                strNum = num
            else:                
                strNum = str(strNum)  + "0"
    else:
        strNum = number
        
    return int(strNum)
  

num2word(2100)
num2word(13)
num2word(1002)
num2word(45667)
num2word(999987)



