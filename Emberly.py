import os
import time
import random


os.system("clear")
time.sleep(1)

# FAMILY TERM GENERATOR
FAMILYTERMS = "Mother", "Father", "Son", "Daughter", "Brother", "Sister", "Aunt", "Uncle", "Cousin", "Neice", "Nephew", "Grandparent", "Grandchild", "In-law", "Stepmother", "Stepfather", "Stepson", "Stepdaughter"

# FIRST NAMES GENERATOR
FIRSTNAMES = ["Alexis", "Jeff", "Jessica", "Ruby", "Trey", "John", "Jake", "Mark", "Jason", "Sarah", "Amy", "Gerald", "Rook", "Nik", "Emma", "Gabi", "Gabriella", "Emily", "Parker", "Don", "Donna", "Linda", "Charles", "Charlie", "Lucas", "Donald", "Vennice", "Victoria", "Sebastian", "Sharon", "Tiffany", "Jay", "Elmer", "Mike", "Nathan", "Greg", "Alexis", "Alexander", "Aaron", "Adrian", "Andrew", "Aahana", "Adam", "Adison", "Alice", "Amari", "Angel", "Anthony", "Ava", "Aaliyah", "Aaradhya", "Abigail", "Achilles", "Amy", "Aimée", "Anders", "Archer", "Audrey", "August", "Bob", "Benjamin", "Bixby", "Brian", "Blake", "Birtha", "Brandon", "Billy", "Bill", "Bobby", "Carol", "Candice", "Cindy", "Cynthia", "Dewy", "Dustin", "Drake", "Eric", "Eden", "Emmma", "Emily"]

# LAST NAME GENERATOR
LASTNAMES = ["Phillips", "Bowden", "Valentine", "Brown", "Jackson", "Henson", "Johnson", "Patel", "Silva", "Wang", "O'Conner", "Henderson", "Smith", "Perkins", "Thompson", "Rose", "Clem", "Pruett", "Sears", "Maxine", "Evelyn"]

# GENDER GENERATOR
GENDERS = ["Agender", "Genderfluid", "Bigender", "Transgender", "Nonbinary", "Pangender","Intersex", "Asexual", "Demigender", "Demiboy", "Genderqueer", "Androgynous", "Female", "Male"]

PRONOUNS = ["She/Her/Hers", "He/Him/His", "They/them/theirs", "Xe/xem/xyrs", "Ze/zir/zirs"]

# JOB GENERATOR
JOBS = ["Engineer", "Electrician", "Entertainer", "Factory Worker", "Chef", "Programmer", "IT", "Security Researcher", "Musician", "Film Producer", "Film Director", "Author", "Court Judge", "Lawyer", "Server", "NOJOB"]

WEAPONS = ["Colt Single Action Army Revolver", "AK-47", "M16 Rifle", "Brass Knuckles", "Scythe"]


# NUMBER GENERATOR
NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# NUMBER GENERATOR
NUM2 = ["3", "4", "5", "6", "7"]

#NUMBER GENERATOR
NUM3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# PROGRAMMING LANGUAGES
PL = ["C", "C++", "C#", "Objective-C", "Javascript", "Ruby", "Python"]

# LOG
# added more hair 10/25/25

# HAIRSTYLES GENERATOR
HAIRSTYLES = ["Mohawk", "Wolf Cut", "Bowl Cut", "Skullet", "Chelsea Cut", "Long Layered Cut", "Bob", "Mullet", "Bixie", "Afro"]

# COLORS
COLORS = ["Red", "Blue", "Yellow", "Green", "Orange", "Purple"]

# print(len(FAMILYTERMS))
# print(len(FIRSTNAMES))
# print(len(LASTNAMES))
# print(len(HAIRSTYLES))
# print(len(COLORS))

# CHOOSE BODY HAIR PERCENTAGE
bhpercentage = random.randint(0, 100)

# CHOOSE LEFT OR RIGHT (< or >) (1)
lor1 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (2)
lor2 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (3)
lor3 = random.randint(0,1)

# CHOOSE LEFT OR RIGHT (< or >) (4)
lor4 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (5)
lor5 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (6)
lor6 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (7)
lor7 = random.randint(0, 1)

# CHOOSE LEFT OR RIGHT (< or >) (8)
lor8 = random.randint(0, 1)

# CHOOSE FAMILY TERM
ft = random.choice(FAMILYTERMS)

# CHOOSE LETTER
letter = random.randint(0, 26)

# CHOOSE FIRST NAME
fn = random.choice(FIRSTNAMES)

# CHOOSE LAST NAME
ln = random.choice(LASTNAMES)

# CHOOSE JOB
jb = random.choice(JOBS)

# CHOOSE PL
pl = random.choice(PL)

# CHOOSE HAIR STYLE
ht = random.choice(HAIRSTYLES)

# CHOOSE GENDER
gender = random.choice(GENDERS)

# CHOOSE PRONOUNS
pronouns = random.choice(PRONOUNS)

# CHOOSE WEAPON
weapons = random.choice(WEAPONS)

# CHOOSE NUMBER (1)
num = random.choice(NUM)

# CHOOSE NUMBER (2)
num2 = random.choice(NUM)

# CHOOSE NUMBER (3)
num3 = random.choice(NUM2)

# CHOOSE NUMBER (4)
num4 = random.choice(NUM2)

# CHOOSE NUMBER (5)
num5 = random.choice(NUM3)

# CHOOSE HAIR COLOR
hc = random.randint(0, 5)

# CHOOSE EYE COLOR (L)
lec = random.randint(0, 5)

# CHOOSE EYE COLOR (R)
rec = random.randint(0, 5)

# CHOOSE ARMPIT HAIR COLOR (L)
lahcolor = random.randint(0, 5)

# CHOOSE ARMPIT HAIR COLOR (R)
rahcolor = random.randint(0, 5)

# CHOOSE CHEST HAIR COLOR
chcolor = random.randint(0, 5)

# CHOOSE STOMAGH HAIR
shcolor = random.randint(0, 5)

# CHOOSE LEG HAIR COLOR (L)
llhcolor = random.randint(0, 5)

# CHOOSE LEG HAIR COLOR
rlhcolor = random.randint(0, 5)

# CHOOSE BACK HAIR COLOR
bhcolor = random.randint(0, 5)

os.system("clear")

# PRINT ART
print("""▄▖▖  ▖▄ ▄▖▄▖▖ ▖▖
▙▖▛▖▞▌▙▘▙▖▙▘▌ ▌▌
▙▖▌▝ ▌▙▘▙▖▌▌▙▖▐ 
                """)

# PRINT FIRST NAME
print("\nYour characters first name: " + fn)

# PRINT LAST NAME
print("Your characters last name: " + ln)

print(" ")

# PRINT HEIGHT
print(fn + "'s height: " + num3 + "'" + num4)

print(" ")

print(fn + "'s gender: " + gender)

print(fn + "'s pronouns: " + pronouns)

# PRINT RELATION
print(fn + "'s relation: " + ft)

print(" ")

if(jb == "Programmer"):
  # PRINT JOB
  print(fn + "'s Job: " + jb)
  print(fn + "'s Programming Language: " + pl)
  
if (jb == "NOJOB"):
  # PRINT X IS JOBLESS
  print(fn + " does not have a job.")
  
if (jb != "NOJOB" and jb != "Programmer"):
  print(fn + "'s job: " + jb)

# PRINT YEARLY INCOME
if (jb == "Programmer"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Engineer"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Author"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")

if (jb == "Electrician"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Chef"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Security Researcher"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "IT"):
  print(fn + "'s yearly salary: $" + num + num2  + ",000")
  
if (jb == "Court Judge"):
  print(fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Musician"):
  print (fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Lawyer"):
  print (fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Film Producer"):
  print (fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Film Director"):
  print(fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Entertainer"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Factory Worker"):
  print(fn + "'s yearly salary: $" + num + num2 + ",000")
  
print(" ")

# PRINT WEAPON IF ANY
if (lor8 == 1):
  print(fn + "'s weapon: " + weapons)
else:
  print(fn + " does not have a weapon.")
  
print(" ")

# PRINT BODY HAIR PERCENTAGE
percent = str(bhpercentage)
print(fn + "'s body hair percentage: " + percent + "%")

# PRINT HAIR STYLE
print(fn + "'s hairstyle: " + ht)
    
# PRINT HAIR COLOR
print(fn + "'s hair color: " + COLORS[hc])
    
# PRINT EYE COLOR (L)
print(fn + "'s left eye color: " + COLORS[lec])

# PRINT EYE COLOR (R)
print (fn + "'s right eye color: " + COLORS[rec])

# PRINT ARMPIT HAIR COLOR (L)
if (bhpercentage > 50):
  print(fn + "'s left armpit hair color: " + COLORS[lahcolor])
else:
  print(fn + " does not have any left armpit hair.")
        
# PRINT ARMPIT HAIR COLOR (R)
if (bhpercentage > 50):
  print(fn + "'s right armpit hair  color: " + COLORS[rahcolor])
else:
  print(fn + " does not have any right armpit hair.")

# PRINT CHEST HAIR COLOR
if (bhpercentage > 50):
  print(fn + "'s chest hair color: " + COLORS[chcolor])
else:
  print(fn + " does not have any chest hair.")
# PRINT STOMACH HAIR COLOR
if (bhpercentage > 50):
  print(fn + "'s stomach hair color: " + COLORS[shcolor])
else:
    print(fn + " does not have any stomach hair.")
# PRINT BACK HAIR COLOR
if (bhpercentage > 50):
  print(fn + "'s back hair color: " + COLORS[bhcolor])
else:
  print(fn + " does not have any back hair")
# PRINT LEG HAIR COLOR (L)
if (bhpercentage > 50):
    print(fn + "'s left leg hair color: " + COLORS[llhcolor])
else:
  print(fn + " does not have any left leg hair.")
# PRINT LEG HAIR COLOR (R)
if (bhpercentage > 50):
  print(fn + "'s right leg hair color: " + COLORS[rlhcolor])
else:
  print(fn + " does not have any right leg hair.")
