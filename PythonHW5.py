# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


#text = input()
#text = text.split()
#new_text = ''

#for i in text:
#    if 'абв' not in i:
#        new_text += 'i' + ''
#print(new_text)

# или функция:

#text = input()
#text = text.split()
#new_text = list(filter(lambda x: 'абв' not in x, text))
#print(new_text)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


#with open('file_encode.txt', 'w') as data:
#    data.write('FFFFFFFFFFPPPPPPPPPPNNNNNNNNN')

#with open('file_encode.txt', 'r') as data:
#    string = data.readline()

#def text_encode(decoded_string):
#    encoded_string = ''
#    count = 1
#    char = decoded_string[0]
#    for i in range(1, len(decoded_string)):
#        if decoded_string[i] == char:
#            count += 1
#        else:
#            encoded_string = encoded_string + str(count) + char
#            char = decoded_string[i]
#            count = 1
#            encoded_string = encoded_string + str(count) + char
#    return encoded_string


#def text_decode(encoded_string):
#    decoded_string = ''
#    char_amount = ''
#    for i in range(len(encoded_string)):
#        if encoded_string[i].isdigit():
#            char_amount += encoded_string[i]
#        else:
#            decoded_string += encoded_string[i] * int(char_amount)
#        char_amount = ''
#    print(decoded_string)
#    return decoded_string


#with open('file_encode.txt', 'r') as file:
#    decoded_string = file.read()

#with open('file_decode.txt', 'w') as file:
#    encoded_string = text_encode(decoded_string)
#    file.write(encoded_string)


#print('Данные после сжатия: \t' + text_encode(decoded_string))
#print('Восстановленные данные: \t' + decoded_string)


# Создайте программу для игры в ""Крестики-нолики"".


maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

victories =  [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8]) 

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"        
    return win

game_over = False
player1 = True
 
while game_over == False:
    print_maps()
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
    step_maps(step,symbol) 
    win = get_result() 
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)        
        
print_maps()
print("Победил", win) 