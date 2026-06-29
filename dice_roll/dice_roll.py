# Logic 
# loop
# ask : roll dice ?
# if ans : yes
#  gen two random nums
#  print them
# if ans : no
#  print thank u msg
#  terminate
#  else 
#  invalid input

import random
while True:
    choice = input( "roll the dice? ( yes / no) : ").lower() 
    if choice == 'yes': # or choice == 'Y'
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif choice =='no':
        print('Thanks for playing!')
        break
    else:
        print("invalid choice")
