from random import shuffle
myList = ['','O','']

def shuffle_my_list(my_list):
    shuffle(my_list)
    return my_list

shuflledList = shuffle_my_list(myList)

# print(shuflledList)

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
       guess= input('Enter a number of ball\'s position(0,1 or 2)\n:')
    return int(guess)

guess =  player_guess()
print(guess)

def check_guess(my_list,guess):
    if my_list[guess] =='O':
        print('CORRECT!!')
    else:
        print('INCORRECT')
        print(my_list)

check_guess(shuflledList,guess)
