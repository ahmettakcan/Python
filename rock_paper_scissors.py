from random import choice

list = ["Rock","Paper","Scissors"]

user_val = 0
machine_val = 0
while True:
  user = input("Rock, Paper, Scissors ?\n")
  machine = choice(list)
  print(machine)
  
  if (user == list[0] and machine == list[2]) or (user == list[2] and machine == list[1]) or (user == list[1] and machine == list[0]):
    print("User won the round")
    user_val+=1
  
  elif (machine == list[0] and user == list[2]) or (machine == list[2] and user == list[1]) or (machine == list[1] and user == list[0]):
    print("Machine won the round")
    machine_val+=1
  
  else:
    print("The round is draw")

  print(f"User's : {user_val} | Machine's : {machine_val}")
  total = input("Do you wanna play again ?\n")

  if total != "yes":
    break

if user_val > machine_val:
  print("User Won")

elif machine_val > user_val:
  print("Machine Won")

else:
  print("Draw")
