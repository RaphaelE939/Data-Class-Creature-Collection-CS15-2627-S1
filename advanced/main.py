from dataclasses import dataclass
import time

@dataclass

class Creature:
    name: str
    species: str
    level: int
    health: float

creature1 = Creature("Zorocard", "Elbloom", 3, 120.5)
creature2 = Creature("Obolo", "Lolong", 1, 67.67)
creature3 = Creature("Ploye", "Kylon", 5, 200.7)
creature4 = Creature(None,None,None,None)

while True:
    player_choice = input("\nWelcome to Build-A-Creature, where you build a creature of your own choosing with its own stats. Have fun!!"
                          "\nWhat would you like your creatures name to be?"
                          "\n")
    str(player_choice.capitalize())
    creature4.name = player_choice

    player_choice = input(f"What would you like {creature4.name}'s species to be?"
                          f"\n")
    str(player_choice.capitalize())
    creature4.species = player_choice
    break


while True:
    player_choice = input(f"What would you like {creature4.name}'s level to be?"
                          f"\n")
    try:
        int(player_choice)
        creature4.level = player_choice
        break
    except ValueError:
        print("This is not a valid integer, try again.")

while True:
    player_choice = input(f"What would you like {creature4.name}'s health value to be? (It can have decimals)."
                          f"\n")
    try:
        float(player_choice)
        creature4.health = player_choice
        break
    except ValueError:
        print("This is not a valid float value, try again.")

print(f"Here is your finished, decked out creature:"
      f"\nName: {creature4.name}"
      f"\nSpecies: {creature4.species}"
      f"\nLevel: {creature4.level}"
      f"\nHealth: {creature4.health}"
)

