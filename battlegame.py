wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
orc_hp = 200

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
orc_damage  = 30

exitGame = 1

while exitGame:
    while True:
        print("1) "+ "  " + wizard)
        print("2) "+ "  " + elf)
        print("3) "+ "  " + human)
        print("4) "+ "  " + orc)
        print("5) EXIT")

        character =input("Choose your character: ")

        if character == "1" or character.upper()=="WIZARD":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "2" or character.upper()=="ELF":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == "3" or character.upper()=="HUMAN":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == "4" or character.upper()=="ORC":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif character =="5" or character.upper()=="EXIT":
            print("Exiting...")
            exitGame = 0
            break
        print("Unknown character")

    if  exitGame:
        print("You have chose the character ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        
        while True:
            dragon_hp-=my_damage
            print("The ", character, "  damaged the Dragon!")
            print("The Dragon's hit point are now", dragon_hp , "\n")
            if dragon_hp<=0:
                print("Dragon has lost the battle \n ")
                tryAgain = input("Do you want to try again? [yes/no]")
                if tryAgain.upper()=="YES":
                    exitGame = 1
                elif tryAgain.upper() == "NO":
                    exitGame = 0  
                    print("exiting")
                break

            my_hp-=dragon_damage
            print("The Dragon strikes back at the ", character)
            print("The ", character, " hit points are now ", str(my_hp), "\n")

            if my_hp<=0:
                print("The ", character, "has lost the battle \n")
                tryAgain = input("Do you want to try again? [yes/no]")
                if tryAgain.upper()=="YES":
                    exitGame = 1
                elif tryAgain.upper() == "NO":
                    exitGame = 0  
                    print("exiting")
                break

