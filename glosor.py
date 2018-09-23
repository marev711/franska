# -*- coding: utf-8 -*-
import random
import itertools
swedish  =  ["var",  "nu",           "synd",     "jag vinner",  "en blomma",    "ett träd",  "en man",    "en motocykel"]
french   =  ["où",   "maintenant",   "dommage",  "je gagne",    "une fleur",    "un arbre",  "un homme",  "une moto"]
len_french=len(french)
index_french=list(range(len_french))
my_permutations=list(itertools.permutations(index_french))
len_myperm=len(my_permutations)
my_permutation=my_permutations[random.randint(0, len_myperm-1)]
print(my_permutation)

for index in my_permutation:
  Answer=input('what is the french for: ' + swedish[index]+"   ")
  if Answer==french[index]:
   print("Correct!")
  else:
   print("Wrong '" + french[index] + "' is the correct answer.")

#english  =  ["zero",  "one",  "two",   "three",  "four",    "five",  "six",  "seven",  "eight",  "nine",  "ten",  "eleven",  "twelve",  "thirteen",  "fourteen",  "fifteen",  "sixteen",  "seventeen",  "eighteen",  "nineteen",  "twenty",  "twenty-one",  "twenty-two",  "twenty-three",  "twenty-four",   "twenty-five",  "twenty-six",  "twenty-seven",  "twenty-eight",  "twenty-nine",  "thirty",  "fourty",    "fifty",      "sixty",     "seventy",       "eighty",        "ninety",            "hundred",  "thousand"]
#french   =  ["zéro",  "un",   "deux",  "trois",  "quatre",  "cinq",  "six",  "sept",   "huit",   "neuf",  "dix",  "onze",    "douze",   "treize",    "quatorze",  "quinze",   "seize",    "dix-sept",   "dix-huit",  "dix-neuf",  "vingt",   "vingt",       "vingt-deux",  "vingt-trois",   "vingt-quatre",  "vingt-cinq",   "vingt-six",   "vingt-sept",    "vingt-huit",    "vingt-neuf",   "trente",  "quarante",  "cinquante",  "soixante",  "soixante-dix",  "quatre-vingt",  "quatre-vingt-dix",  "cent",     "mille"]

