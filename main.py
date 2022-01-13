import random 
import os

data = open("data.txt", "r")
content_list = data.readlines()

question = []
answer = []
voltmar = []

pontok = 0
osszesen = 0

data.close()

for i in range(0,len(content_list)):
    split = content_list[i].split('#')
    question.append(split[0])
    answer.append(split[1].strip())

while True:
    os.system('cls||clear')

    index = random.randint(0, len(content_list)-1)
    while index in voltmar:
        index = random.randint(0, len(content_list)-1)

    if osszesen >= 1:
        szazalek = (pontok/osszesen)*100
        print(f"Megválaszolt kérdések: {osszesen} - Helyes válaszok: {pontok}. ({szazalek}%)\n")

    print(question[index])
    player_answer = input("Válasz: ")

    if player_answer.upper() == answer[index]:
        print(f"Helyes megoldás!! ({answer[index]})")
        pontok += 1
        osszesen += 1
    elif player_answer.upper() == 'E':
        exit()
    else:
        print(f"Rossz megoldás!! ({answer[index]})")
        osszesen += 1

    voltmar.append(index)
    if len(voltmar) == len(content_list):
        exit()
    else:
        input("Nyomj Entert a folytatáshoz...")