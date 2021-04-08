# File: hw1c.py
# Author: Sam Waggoner
# Date: 09/11/2020 (edited 09/18/2020)
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write some basic code and debug it. In part C we find the total and average
# of seven integer inputs and print using those values.
# Collaboration:
# I did not collaborate with anyone. I loopked up solutions for strings and
# equations over multiple lines (using \ and """).

gameone = int(input("How many points did Kemba Walker score in Game 1?", ))
gametwo = int(input("How many points did Kemba Walker score in Game 2?", ))
gamethree = int(input("How many points did Kemba Walker score in Game 3?", ))
gamefour = int(input("How many points did Kemba Walker score in Game 4?", ))
gamefive = int(input("How many points did Kemba Walker score in Game 5?", ))
gamesix = int(input("How many points did Kemba Walker score in Game 6?", ))
gameseven = int(input("How many points did Kemba Walker score in Game 7?", ))
total_points = gameone + gametwo + gamethree + gamefour + gamefive + gamesix \
    + gameseven
average = total_points / 7
print("Kemba Walker scored",total_points,"""points over the course of the NBA 
East Semifinals, yielding an average of""",average,"points per game.")

# Or using loops
# Both of these are wrong.
game = 1
for i in range(1,8):
    total = int(input("How many points did Walker score in game",game,"?", ))
    total += total
    game += 1
print(total)
print(total/7)


i = 1
game = 1
while i < 8:
    points = int(input("How many points did my man Kemba score in game",game,"?"))
    points += points
    i += 1
    game += 1
print(points)