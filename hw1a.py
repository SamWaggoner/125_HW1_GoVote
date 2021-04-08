# File: hw1a.py
# Author: Sam Waggoner
# Date: 09/11/2020 (edited 09/18/2020)
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write some basic code and debug it. In part a we prompt for a string and
# print responses with that string within it.
# Collaboration:
# I asked Zachary Hutchinson about how to get rid of the spaces when doing print
# statements, and he showed me the sep="" function as well as combining inegers
# together after casting them as strings, although I didn't use that here.

name = str(input("Hi, friend! What's your name? ", ))
print("Hi, ",name,", I'm happy to meet you.",sep="")
print("Let's go register to vote.")