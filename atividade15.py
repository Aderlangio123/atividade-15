# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

numero1 = float(input("digite o primeiro numero! :  "))
numero2 = float(input("digite o segundo numero! :  "))
operacao = str(input("digite a operação desejada! soma,subtraçao,multiplicaçao ou divisao?  :  "))

if operacao == "soma":
    print("o resultado é", " ", numero1 + numero2)

elif operacao == "subtraçao":
       print("o resultado é", " ", numero1 - numero2)

elif operacao == "multiplicaçao":
       print("o resultado é", " ", numero1 * numero2)

elif operacao == "divisao":
      print("o resultado é", " ", numero1 / numero2)
      