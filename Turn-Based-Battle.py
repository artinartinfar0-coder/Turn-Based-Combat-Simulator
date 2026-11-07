import time
import random
class Character:
    def __init__(self,name,hp=100,attack_power=15):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    def attack(self,target):
        damage = random.randint(self.attack_power - 5,self.attack_power + 5)
        if random.random() < 0.2:
            damage *= 2
            print("CRITICAL HIT !")
            target.hp -= damage
            print(f"{self.name} attacks{target. name} for {damage} damage!")
hero = Character("Hero",100,20)
monster = Character("Dragon", 120,15)
while hero.hp > 0 and monster.hp > 0:
    hero.attack(monster)
    time.sleep(1)
    if monster.hp <= 0:
        break
    monster.attack(hero)
    time.sleep(1)
    if hero.hp <= 0:
        break
print(f"Status -> Hero: {hero.hp} HP | Dragon: {monster.hp} HP")
print("-" * 30)
if hero.hp > 0:
    print("Hero Wins!")
else:
    print("Dragon Wins!")