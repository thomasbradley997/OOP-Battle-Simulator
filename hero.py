<<<<<<< Updated upstream
=======
import random
from enemy import Enemy
>>>>>>> Stashed changes
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        #TODO Set the hero's name.
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
<<<<<<< Updated upstream
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def receive_damage(self, damage):
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
=======
        return random.randint(self.attack_power, 100)
    hero_health = 0
    def receive_damage(self, damage):
        self.damage = self.strike(Enemy)
        self.health -= self.damage
        if self.health <= 0:
            self.health = 0
            return self.damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
>>>>>>> Stashed changes
    
    #TODO define is_alive
