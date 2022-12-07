#!/usr/bin/env/python3

#Fix code:

print("Day 1 - String Manipulation")

print("String Concatenation is done with the \"+\" sign.")

print('e.g. print("Hello " + "world")')

print("New lines can be created with a backslash and n.")

#fixed code:

print(Day 1 - String Manipulation")                        <-- missing a quote
print("String Concatenation is done with the "+" sign.")   <-- missing escape sequence for quotes
print('e.g. print("Hello " + "world")')                  <-- uneccessary indentation
print(("New lines can be created with a backslash and n.") <-- uneccessary extra open parenthesis
