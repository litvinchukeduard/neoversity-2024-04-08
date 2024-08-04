from dataclasses import dataclass
from copy import copy, deepcopy
from datetime import datetime
"""
Описати клас, який зберігає інформацію про персонажа з гри (name, health)
"""


# class HealthIsNotValidError(Exception):

class HealthIsNotValidError(ValueError):
    pass


class HealthIsNotIntError(HealthIsNotValidError):
    pass


class HealthIsLessThanZeroError(HealthIsNotValidError):
    pass


# class Item:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price
@dataclass(frozen=True)
class Item:
    name: str
    price: float = 100.0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError


class Character:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name

        self.__health = None
        self.health = health
        # self.health = health
        # return
        self.inventory = []
        self.creation_date = datetime.now()

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        # if not isinstance(new_health, int):
        if type(new_health) != int:
            raise HealthIsNotIntError("Health should be of type int")
        if new_health < 0:
            raise HealthIsLessThanZeroError
        self.__health = new_health

    # def __copy__(self):
    #     new_character = Character(self.name, self.health)
    #     new_character.inventory = self.inventory
    def __copy__(self):
        cls = self.__class__
        new_character = cls.__new__(cls)
        new_character.__dict__.update(self.__dict__)
        new_character.creation_date = datetime.now()
        new_character.name += " Clone"
        return new_character
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        new_character = cls.__new__(cls)
        memo[id(self)] = new_character
        for key, value in self.__dict__.items():
            # new_character.__dict__[key] = deepcopy(value, memo)
            # if key == 'creation_date':

            setattr(new_character, key, deepcopy(value, memo)) # new_character.name = deepcopy("Hero 2", memo)
        new_character.creation_date = datetime.now()
        return new_character

    def __str__(self) -> str:
        # for key, value in self.__dict__.items():
        return f'Character(name = {self.name}, health = {self.health})'
    

class Hero(Character):
    pass

# sword = Item("Sword 1", 200.0)
# hero = Hero("Hero 2", -100)

# print(hero.__dict__)

# hero_copy = deepcopy(hero)
# # hero_copy.creation_date = datetime.now()
# # print(dir(hero_copy))

# # hero.health -= 20
# # hero.inventory.append(sword)

# print(hero.creation_date)
# print(hero_copy.creation_date)
# sword = Item("Sword 1", 200.0)
# sword.price = -100

# hero = Hero("Hero 1")
# print(isinstance(hero, Character))

# character = Character("Hero", True)
# print(character)

# print(dir(character))

# character.health = 100

# print(character._Character__health)
# character.health = "-100"
# print(character.health)

try:
    hero = Hero("Hero 2", -100)
except HealthIsLessThanZeroError:
    print("Hello")
except HealthIsNotValidError:
    print("Error has happened")
except ValueError:
    print("Hello, value")

