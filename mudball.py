"""
Welcome to a simple game that demonstrate the use of functions
this game is called "Mball" and the players take turns lobbing mball at each other until someone gets hit.
"""

import math
import random

def print_instructions():
    print("""
          Welcome to Mball the idea is to hit the other player with a mudball.
          Enter your angle (in degrees) and the amount of PSI to change your gun with.
          """)

def calculate_distance(psi, angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians)
    return distance

def get_user_input(name):
    psi = float(input(name + "charge the gun with how many psi?"))
    angle = float(input(name + "move the gun at what angle?"))
    return psi, angle

def get_player_name():
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit):")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
        
    print()
    return players

def process_player_turn(player_name, distance_apart):
    psi, angle = get_user_input(player_name)
    
    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart
    
    if difference > 1:
        print("You went", difference, "yards too far!")
        
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
        
    else:
        print("Hit!", player_name, "wins!")
        return True
    
    print()
    return False

def main():
    print_instructions()
    player_names = get_player_name()
    distance_apart = random.randrange(50, 150)
    
    done = False
    while not done:
        # loop for each player
        for player_name in player_names:
            #process their turn
            done = process_player_turn(player_name, distance_apart)
            # if someone won, 'break'out of the loop and end the game.
            if done:
                break
        
if __name__ == "__main__":
    main()
            