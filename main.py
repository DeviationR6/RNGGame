import random
from clint.textui.colored import red, green, magenta, cyan
# create a computer that will randomly select rock paper scissors
# handle different states and say if you win or not
dict_key = {0 : "rock" , 1 : "paper" , 2 : "scissors"}
comp = dict_key[random.randint (0,2)]
human = input (magenta('Enter Rock, Paper or Scissors: ').lower())

print(cyan("Computer: {c}, Human: {h}\n".format(c=comp, h=human)))

if human not in dict_key.values():
  print(red('enter in a functioning value u bot'))
elif comp == human:
  print (red('TIE so TRY AGAIN SUCKERRRRR'))
elif comp == "rock" and human == "paper":
  print (green('winner lol'))
elif comp == "paper" and human == "scissors":
  print (green('winner lol'))
elif comp == "scissors" and human == "rock":
  print (green('winner lol'))
else:
  print (red('u are a bot cuz u lost lol'))