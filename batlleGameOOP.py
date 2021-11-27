class Character():
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
        name_list = [].append(self.name)
        hp_list = [].append(self.hp)
        damage_list = [].append(self.damage)
    
    def printOption(self):
        i = 1
        for name in name_list:
            print(i,") ",name )

    
wizard = Character("Wizard", 70, 150)
human = Character("Human", 150, 20)
Character.printOption()