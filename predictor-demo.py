from sklearn.naive_bayes import ComplementNB
import pandas as pd
import numpy as np
import pickle
import csv
import os

def print_line():
    print("=====================================\n")

team = []

# Load machine learning models
ability_cnb = pickle.load(open('ability_cnb.sav', 'rb'))
item_cnb = pickle.load(open('item_cnb.sav', 'rb'))
moves_cnb = pickle.load(open('moves_cnb.sav', 'rb'))

# Load the list of VALID POKEMON
with open('VALID_POKEMON.csv', newline='') as csvfile:
    valid_pokemon = list(csv.reader(csvfile))

valid_pokemon = valid_pokemon[0]
valid_pokemon = [x.lower() for x in valid_pokemon]

os.system('cls')
print("\nPokemon Team Predictor")
print_line()
print("Please check VALID_POKEMON.csv for a list of valid pokemon.")

# TAKE INPUT
print("Enter a team of six pokemon (separated by new lines):")

while len(team) < 6:
    pokemon = input()

    if pokemon.lower() in valid_pokemon:
        team.append(pokemon.lower())
    else:
        print("Invalid Pokemon name, please input again:")

print_line()
print(f"Team successfully inputted: {team}")

input("\nPress Enter to continue...")

pred_ability = []
pred_item = []
pred_moves = []

# Predict items moves abilities for each team member
for focus in team:
    # Build input Array
    focus_array = [0 for _ in valid_pokemon]
    focus_array[valid_pokemon.index(focus)] = 1

    team_array = [0 for _ in valid_pokemon]
    for teammate in [x for x in team if x != focus]:
        team_array[valid_pokemon.index(teammate)] += 1

    input_array = focus_array + team_array
    
    # Prediction
    ability = ability_cnb.predict(np.reshape(input_array, (1, -1)))
    pred_ability.append(ability[0])
    
    item = item_cnb.predict(np.reshape(input_array, (1, -1)))
    pred_item.append(item[0])

    proba = moves_cnb.predict_proba(np.reshape(input_array, (1, -1)))
    moves_proba = list(zip(proba[0], moves_cnb.classes_))
    moves_proba.sort(reverse=True)
    pred_moves.append((moves_proba[0][1], moves_proba[1][1], moves_proba[2][1], moves_proba[3][1]))

os.system('cls')

# Predict items moves abilities for each team member
for i in range(len(team)):
    print_line()
    print(team[i])
    
    print(f"Predicted Ability: {pred_ability[i]}")
    print(f"Predicted Item: {pred_item[i]}")
    print(f"Predicted Moves: {pred_moves[i]}")
