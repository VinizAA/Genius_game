import random
import time
import os
import sys
import getch

def read_digits():
    digitos = []

    tecla = getch.getch()
    if tecla.isdigit():
        digitos.append(tecla)
        print(tecla, end='', flush=True)
    
    return digitos

def clear():
    if os.name == 'posix':  
        os.system('clear')
    else: 
        os.system('cls')

def generate_seq(size):
    temp_list = []
    while len(temp_list) < size:
        num = random.randint(0, 9)
        if num not in temp_list:
            temp_list.append(num)
    return temp_list

def main():
    size = 0  
    while True:
        choice = 0

        while choice not in ['1', '2', '3']:
            clear()
            print('DEFINE THE DIFFICULTY')
            print('[1] Easy')
            print('[2] Medium')
            print('[3] Hard')

            choice = input('\n>> ')

            if choice == '1':
                size = 3
            elif choice == '2':
                size = 5 
            elif choice == '3':
                size = 10 
            else:
                print('Invalid choice. Please choose a valid option.')
                time.sleep(2)

        seq_list = generate_seq(size)

        clear()
        for num in seq_list:
            print("WAIT!")
            print(num)
            time.sleep(1)
            clear()

        user_nums = []
        for _ in range(size):
            print("YOUR TURN")
            user_nums.append(read_digits())
            time.sleep(0.14)
            clear()

        # Convertendo user_nums para uma lista de inteiros
        user_nums_int = [int(num[0]) for num in user_nums]

        if seq_list == user_nums_int:
            print("VOCÊ GANHOU!!")
        else:
            print("VOCÊ PERDEU!!")

        print("\nDeseja recomeçar?")
        print("[1] SIM")
        print("[2] NÃO")

        restart = input('\n>> ')

        if restart == '1':
            continue
        elif restart == '2':
            exit()

if __name__ == "__main__":
    main()
