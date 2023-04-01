# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto, em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

quantidade_rodas = 6
peso_bruto = 7000
quantidade_pessoas = 9

if(quantidade_rodas >= 1 and quantidade_rodas <= 3):
    print("Categoria da CNH pare este veículo é: A")
elif(quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500):
    print("Categoria da CNH pare este veículo é: B")
elif(quantidade_rodas >= 4 and peso_bruto >= 3500 and peso_bruto <= 6000):
    print("Categoria da CNH pare este veículo é: C")
elif(quantidade_rodas >= 4 and quantidade_pessoas > 8):
    print("Categoria da CNH pare este veículo é: D")
elif(quantidade_rodas >= 4 and peso_bruto > 6000):
    print("Categoria da CNH pare este veículo é: E")