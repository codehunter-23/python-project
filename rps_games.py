import random
print('\n')
print('This game will have the following rules : \n\n'
+ 'Rock VS Paper -> the winner is PAPER \n'
+ 'Rock VS Scissor -> the winner is ROCK \n'
+ 'Paper VS Scissor -> the winner is SCISSOR \n')

while True:
    print('Well, you can enter your choices number : \n\n 1. Rock \n 2. Paper \n 3. Scissor \n')
    choices = int(input('Your turn: '))
    while choices > 3 or choices < 1:
        choices = int(input('Enter your valid input here: '))
    if choices == 1:
        choice_name = 'Rock'
    elif choices == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    print('Your choices is: ' + choice_name + '\n')
    print('Now the computer will turn to initiate.....')
            
    computer_choice = random.randint(1,3)
    while computer_choice == choices:
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            computer_choice_name = 'Rock'
        elif computer_choice == 2:
            computer_choice_name = 'Paper'
        else:
            computer_choice_name = 'Scissor'
        print('Computer choice is: ' + computer_choice_name + '\n')
        print('== ' + choice_name + ' VS ' + computer_choice_name + ' ==\n')
                        
        if((choices == 1 and computer_choice == 2) or
        (choices == 2 and computer_choice == 1)):
            print('== The winner is PAPER ==\n', end = '')
            final_result = 'Paper'
        elif ((choices == 1 and computer_choice == 3) or
        (choices == 3 and computer_choice == 1)):
            print('== The winner is ROCK ==\n', end = '')
            final_result = 'Rock'
        else:
            print('== COMPUTER WINS == \n')

        print('\n')
        print('Hey, do you want to play again? (Y/N)')
        answer = input()

        if answer == 'n' or answer == 'N':
            break
        else:
            print('Thank your for playing with us :)\n')