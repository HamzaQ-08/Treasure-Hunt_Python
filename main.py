import time

print("Welcome to treasure hunt")
print("\nYour mission is to find the treasure")
print("\nApp k samne ek nadi(RIVER) h or apke pas cross karne k 2 option h \n\n1. Swim karke jao\n2. Boat se jao")
while True:
  choice1 = int(input("\nEnter your choice[1 or 2]: "))
  if choice1 == 1:
    print("Swimming......")
    time.sleep(3)
    print("\nAap kinare par phoch chuke ho")
    break
  elif choice1 == 2:
    print("In Mid of River......")
    time.sleep(3)
    print("\nAapki Boat m Hole ki wajah se pani bhar gya h \n aap dub gay 'GAME OVER' ")
  else:
    print("\nEnter a valid choice")
    break
while True:
  print("\nApke Samne 2 Raste hai\n1. Pehla jaha koi nahi gaya waha par bohot jhadiya hai\n2. Jaha Bohot se pero k nishan h ")
  
  choice2 =int(input("\nEnter your choice[1 or 2]: "))
  if choice2 == 1:
    print("Walking.......")
    time.sleep(3)
    print("\nAap Busan Sheher m hai or apko Zombies ne maar diya \n 'GAME OVER'")
    break
  elif choice2==2:
    print("Walking.......")
    time.sleep(3)
    print("\nAapke safe hai or apne samne ek pahad hai ")
    break
  else:
    print("\nEnter a Valid Value")
    break

while True:
  print("\nAapke samne ek pahad hai or aapke pass ek gufa hai\n1. Aapko gufa me jaoge \n2. Aap pahad p chadoge")
  choice3 =int(input("\nEnter your choice[1 or 2]: "))
  if choice3 == 1:
    print("Very Dark.......")
    time.sleep(3)
    print("\nAapke samne Bhalu aa gya usne aapko maar diya\n 'GAME OVER'")
  elif choice3 == 2:
    print("Climbing.......")
    time.sleep(3)
    print("\nAap Pahad p chad gay ho Jaha aapko khazana bhi mil gaya\n 'YOU WIN'")
    break
  else:
    print("\nINTER A VALID CHOICE")
    
