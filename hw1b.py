# File: hw1b.py
# Author: Sam Waggoner
# Date: 09/11/2020 (edited 09/18/2020)
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write some basic code and debug it. In part B we ask for an integer price and
# do calculations with it then print a result.
# Collaboration:
# I asked Zachary Hutchinson about how to get rid of the spaces when doing print
# statements, and he showed me the sep="" function as well as combining inegers
# together after casting them as strings, although I didn't use that here.

price = int(input("How much is this ice cream bar? ", ))
total_cost = 2 * price * 1.055
print("I would like two bars. Here is $",total_cost,".",sep="")
print("Thank you.")