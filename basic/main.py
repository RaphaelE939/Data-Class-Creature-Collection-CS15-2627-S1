from dataclasses import dataclass

@dataclass

class Creature:
    name: str
    species: str
    level: int
    health: float

creature1 = Creature("Zorocard", "Elbloom", 3, 120.5)
creature2 = Creature("Obolo", "Lolong", 1, 67.67)
creature3 = Creature("Ploye", "Kylon", 5, 200.7)

print(creature1.name)
print(creature1.species)
print(creature1.level)
print(creature1.health)
print("\n")
print(creature2.name)
print(creature2.species)
print(creature2.level)
print(creature2.health)
print("\n")
print(creature3.name)
print(creature3.species)
print(creature3.level)
print(creature3.health)
creature3.level = 22
creature3.health = 300.67676
print("NEW")
print("\n")
print(creature3.health)
print(creature3.level)
print("\n")
print(creature2.health)
print(creature2.level)
print("\n")
print(creature1.health)
print(creature1.level)