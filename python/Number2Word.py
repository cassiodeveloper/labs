import os
# http://pt.wikipedia.org/wiki/Zetta
# http://pt.wikipedia.org/wiki/Escalas_curta_e_longa

from math import log

pattern =  [        
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


shortScale = (
        (1,(" ", " ")),
        (2,("mil", "mil")),
        (3,("milhão", "milhões")),
        (4,("bilhão", "bilhões")),
        (5,("trilhão", "trilhões")) ,
        (6,("quatrilhão","quatrilhões")) ,
        (7,("quintilhão",  "quintilhões")),
        (8,("sextilhão",  "sextilhões")),
        (9,("septilhão",  "septilhões")) 
)

def scienticNotation(number):        
    power =  (int)(log(number) / log(10));
    fraction = (number / pow(10,power))
    print("notation {0} is  {1} * (10^{2}) ".format(number,fraction,power) )


def between(value, bet1, bet2):
     return bool((bet1 < value) and (value < bet2));


def num2word(number):
    print("Número: ",number)
    strOut = ""
    aux = False        
    if number < 1000:
       strOut = write999(number)
    else:        
        # obtem a terna do número
        terns = []
        x  = number        
        while x >= 1:
            itemTern = x % 1000
            terns.append(int(itemTern))
            x /= 1000
                
        count = len(terns)
        
        for item in reversed([a for a in shortScale if a[0] <= count]):            
            currIndex = count - 1
            currentTern = terns[currIndex]
            #print("current",currentTern,"index",currIndex)
            if currentTern == 0 :                
                #strOut = strOut[0: (len(strOut)-1)]                
                count -= 1    
                continue
            
            plural = (currentTern > 1)
            strOut +=  write999(currentTern) + " " + (item[1][1] if plural else item[1][0]) + " " 
            count -= 1
               
    print(strOut)


        
def write999(number):    
    strAux = ""
    divRest = ""
    if number == 0 :
        strAux = "zero"
        return strAux
    
    while True:    
        if number <= 20:
            strAux = findPattern(number);
            break
            
        if strAux == "" and  divRest == "":                                    
            strAux =  findPattern(number)
            divRest = int(number % setNumber(number))            
            aux =  True
            if divRest == 0:
                break
        else:            
            if aux == False:
                divRest = int(divRest % setNumber(divRest))
                if divRest == 0:
                    break
            else:
                divRest = divRest
                        
            strAux += " e " + findPattern(divRest)
            aux = False

    return strAux        


def findPattern(number):    
    for item in pattern:
        value = item[0]
        if value == setNumber(number):
             return str(item[1])


def setNumber(number):
    strNum = ""
    if number > 19:        
        for num in iter(str(number)):            
            if strNum == "":                
                strNum = num
            else:                
                strNum += "0"
    else:
        strNum = number
        
    return int(strNum)
  

       
num2word(534534534)
num2word(0)










