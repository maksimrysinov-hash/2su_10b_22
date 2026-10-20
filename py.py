import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        dmg = random.randint(1, 20)
        target.health -= dmg
        print(self.name + ' attacks: ' + str(dmg))

    def heal(self):
        health = random.randint(1, 20)
        self.health += health
        print(self.name + ' heals: ' + str(health))

john = Character('John', 100)
alex = Character('Alex', 150)
round_number = 1

while john.health > 0 and alex.health > 0:
    print('Round ' + str(round_number))
    
    john.attack(alex)
    if alex.health > 0:
        alex.attack(john)
        
    if round_number % 2 == 0:
        if john.health > 0: john.heal()
        if alex.health > 0: alex.heal()
        
    print('HP -> John: ' + str(john.health) + ' | Alex: ' + str(alex.health))
    
    choice = input('Do you want to playanother round? (y/n): ')
    if choice.lower() != 'y':
        break
        
    round_number += 1

if john.health == alex.health:
    print("Tie")
else:
    winner = 'John' if john.health > alex.health else 'Alex'
    print('Winner is ' + winner)