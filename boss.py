import random
from enemy import Enemy
from hero import Hero

class boss(Enemy):
    def strike(self):
        if self.health >= 60:
            self.attack_power = 40
        return random.randint(self.attack_power)
    
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.attack_power = random.randint(10, 100)