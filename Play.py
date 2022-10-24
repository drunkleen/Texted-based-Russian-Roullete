import random as ran
play_counts = 0
while True:
    print("\n******Hello Welcome To Russian Roullete******\n") if play_counts < 1 else\
        print("\n******Ready To Try Again? Lets Find Out******\n")
    shotx = ran.randrange(1,6)
    bullet_slot = ran.randrange(1,6)
    while True:
        choice = input("\nPress '1' to shoot the current slot \
        \nPress '2' to rotate the revolver\nWhat would be your choice: ")
        if choice == "1":
            if shotx == bullet_slot:
                rematch = input("you're dead =(\n Rematch? (Yes/No): ")
                if rematch  == "no" or rematch == "No":
                    exit()
                else:
                    break
            else:
                print(shotx)
                if shotx < 6:
                    shotx += 1
                else:
                    shotx = 1
                print("you shot and survived")                
        elif choice == "2":     
            if shotx < 6:
                shotx += 1
            else:
                shotx = 1
        else:
            print("\n----you can only choose between 1 and 2----")
    play_counts += 1
