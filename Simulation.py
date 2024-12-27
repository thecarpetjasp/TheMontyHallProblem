# This is the 3 door game
import random

class Game:
    def __init__(self):
        # Initiate the score. This allows you to re-run the simulation to span more games/rounds without losing progress, if that is what you want.
        self.score = 0
    def generate_doors(self):
        # DOOR GENERATION FUNCTION: Here we can initialise the doors for each round. Three doors with only one door containing the million dollars.
        # For this simulation, we will be using 0's and 1's to represent boolean values. 0/False represents a goat. 1/True represents the money.
        # First, create an array of three items that are all 0/False.
        doors = [0]*3
        # Now we choose a random number between 0 and 2, a total of 3 possibilities.
        moneyPos = random.randint(0, 2)
        # We take that number and select an object in our array at that index, and we make it a 1. This represents our door with the million dollars.
        doors[moneyPos] = 1
        return doors
    def stayOrSwitch(self, switch: bool, rounds: int):
        # Looping by the number of chosen rounds to simulate a game.
        for x in range(0, rounds):
            # Generate our doors with only 1 door containing the million dollars behind it, using our generate_doors function.
            doors = self.generate_doors()
            # We choose a random number between 0 and 2, a total of 3 possibilities.
            doorSelection = random.randint(0, 2)
            # Using the random number, we select a door at that index, giving us our first initial selection of a door.
            chosen = doors[doorSelection]
            # We remove our chosen door from the array, leaving us with the other two doors we didn't select.
            del doors[doorSelection]
            # Here, we remove a door from the two remaining doors that contain a 0. This simulates the game show host revealing a door with the goat, leaving us with one more door closed.
            del doors[doors.index(0)]
            # We assign the last remaining unopened door to a variable named unopened.
            unopened = doors[0]
            # If you run this simulation with the 'switch' set to True, we change our selection to the other door that is closed. If we leave 'switch' to False, then we stay with our initial chosen door.
            if switch:
                chosen = unopened
            # Finally, we check if our door contains the million dollars. If true, we increment our score by one point.
            if chosen:
                self.score+=1
        # After all simulated rounds, we now output our total wins and calculate a success rate percentage.
        return f"{self.score}/{rounds} games won.\nThis is a {(self.score/rounds)*100}% success rate."



if __name__ == "__main__":
    # Below is the code to run this simulation. Enjoy!
    rounds = int(input("How many rounds do you want to play?: "))
    switch = input("Would you like to switch? [y/n]: ")
    if switch == ("y"):
        switch = True
    else:
        switch = False
    game = Game()
    result = game.stayOrSwitch(switch, rounds)
    print(result)


# This program was made by TheCarpetJasp.