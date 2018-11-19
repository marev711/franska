# -*- coding: utf-8 -*-
import pdb
import random
import itertools
swedish  =  ["en ko",     "en gris",   "en kanin", "ett marsvin",       "en get",     "en hamster", "en häst",   "en apa",   "en papegoja",  "en katt", "en mus",     "en tiger", "en haj",    "en råtta", "en näbbmus",     "djur"]
french   =  ["une vache", "un cochon", "un lapin", "un cochon d'Inde", "une chèvre", "un hamster", "un cheval", "un singe", "un perroquet", "un chat", "une souris", "un tigre", "un requin", "un rat",   "une musaraigne", "animaux"]
len_french=len(french)
index_french=list(range(len_french))
fel = []
fel2 = []
random.shuffle(index_french)

for index in index_french:
  Answer=input('what is the french for: ' + swedish[index]+"   ")
  if Answer==french[index]:
   print("Correctement!")
  else:
   fel.append(french[index])
   fel2.append(swedish[index])
   print("Ce n'est pas correct! '" + french[index] + "' is the correct answer")

index_fel=list(range(len(fel)))

for index in index_fel:
    Answer=input('what is the french for: ' + fel2[index]+"   ")
    if Answer==fel[index]:
      print("Correctement!")
    else:
      print("Ce n'est pas correct!")
#pdb.set_trace()

#swedish  =  ["blå",  "vit",   "röd",   "gul",   "grön", "svart", "brun",   "brun (ögon)", "lila",  "turkos",   "beige", "grå",  "orange", "rosa", "mörkgrön",   "ljusblå"]
#french   =  ["bleu", "blanc", "rouge", "jaune", "vert", "noir",  "marron", "brun",        "lilas", "turquois", "beige", "gris", "orange", "rose", "vert foncé", "bleu clair"]
#english =  ["zero",  "one",  "two",   "three",  "four",    "five",  "six",  "seven",  "eight",  "nine",  "ten",  "eleven",  "twelve",  "thirteen",  "fourteen",  "fifteen",  "sixteen",  "seventeen",  "eighteen",  "nineteen",  "twenty",  "twenty-one",  "twenty-two",  "twenty-three",  "twenty-four",   "twenty-five",  "twenty-six",  "twenty-seven",  "twenty-eight",  "twenty-nine",  "thirty",  "fourty",    "fifty",      "sixty",     "seventy",       "eighty",        "ninety",            "hundred",  "thousand"]
#french   =  ["zéro",  "un",   "deux",  "trois",  "quatre",  "cinq",  "six",  "sept",   "huit",   "neuf",  "dix",  "onze",    "douze",   "treize",    "quatorze",  "quinze",   "seize",    "dix-sept",   "dix-huit",  "dix-neuf",  "vingt",   "vingt",       "vingt-deux",  "vingt-trois",   "vingt-quatre",  "vingt-cinq",   "vingt-six",   "vingt-sept",    "vingt-huit",    "vingt-neuf",   "trente",  "quarante",  "cinquante",  "soixante",  "soixante-dix",  "quatre-vingt",  "quatre-vingt-dix",  "cent",     "mille"]

swedish  =  ["var",  "nu",           "synd",     "jag vinner",  "en blomma",    "ett träd",  "en man",    "en motocykel"]
french   =  ["où",   "maintenant",   "dommage",  "je gagne",    "une fleur",    "un arbre",  "un homme",  "une moto"]
