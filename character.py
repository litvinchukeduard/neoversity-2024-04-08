from dataclasses import dataclass
"""
Описати клас, який зберігає інформацію про персонажа з гри (name, health)
"""


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

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        # if not isinstance(new_health, int):
        if type(new_health) == int:
            raise ValueError
        if new_health < 0:
            raise ValueError
        self.__health = new_health

    def __str__(self) -> str:
        # for key, value in self.__dict__.items():
        return f'Character(name = {self.name}, health = {self.health})'
    

class Hero(Character):
    pass


sword = Item("Sword 1", 200.0)
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
