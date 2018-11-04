# -*- coding: utf-8 -*-
import random
import itertools
swedish  =  ["blå",  "vit",   "röd",   "gul",   "grön", "svart", "brun",   "brun (ögon)", "lila",  "turkos",   "beige", "grå",  "orange", "rosa", "mörkgrön",   "ljusblå"]
french   =  ["bleu", "blanc", "rouge", "jaune", "vert", "noir",  "marron", "brun",        "lilas", "turquois", "beige", "gris", "orange", "rose", "vert foncé", "bleu clair"]
len_french=len(french)
index_french=list(range(len_french))
random.shuffle(index_french)

for index in index_french:
  Answer=input('what is the french for: ' + swedish[index]+"   ")
  if Answer==french[index]:
   print("Correct!")
  else:
   print("Wrong '" + french[index] + "' is the correct answer.")

#english  =  ["zero",  "one",  "two",   "three",  "four",    "five",  "six",  "seven",  "eight",  "nine",  "ten",  "eleven",  "twelve",  "thirteen",  "fourteen",  "fifteen",  "sixteen",  "seventeen",  "eighteen",  "nineteen",  "twenty",  "twenty-one",  "twenty-two",  "twenty-three",  "twenty-four",   "twenty-five",  "twenty-six",  "twenty-seven",  "twenty-eight",  "twenty-nine",  "thirty",  "fourty",    "fifty",      "sixty",     "seventy",       "eighty",        "ninety",            "hundred",  "thousand"]
#french   =  ["zéro",  "un",   "deux",  "trois",  "quatre",  "cinq",  "six",  "sept",   "huit",   "neuf",  "dix",  "onze",    "douze",   "treize",    "quatorze",  "quinze",   "seize",    "dix-sept",   "dix-huit",  "dix-neuf",  "vingt",   "vingt",       "vingt-deux",  "vingt-trois",   "vingt-quatre",  "vingt-cinq",   "vingt-six",   "vingt-sept",    "vingt-huit",    "vingt-neuf",   "trente",  "quarante",  "cinquante",  "soixante",  "soixante-dix",  "quatre-vingt",  "quatre-vingt-dix",  "cent",     "mille"]

swedish  =  ["var",  "nu",           "synd",     "jag vinner",  "en blomma",    "ett träd",  "en man",    "en motocykel"]
french   =  ["où",   "maintenant",   "dommage",  "je gagne",    "une fleur",    "un arbre",  "un homme",  "une moto"]

