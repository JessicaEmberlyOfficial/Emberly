import os
import time
import random


os.system("clear")
time.sleep(1)

# FAMILY TERM GENERATOR
FAMILYTERMS = "Mother", "Father", "Son", "Daughter", "Brother", "Sister", "Aunt", "Uncle", "Cousin", "Neice", "Nephew", "Grandparent", "Grandchild", "In-law", "Stepmother", "Stepfather", "Stepson", "Stepdaughter"

# FIRST NAMES GENERATOR
FIRSTNAMES = "Alexis", "Jeff", "Jessica", "Ruby", "Trey", "John", "Jake", "Mark", "Jason", "Sarah", "Amy", "Gerald", "Rook", "Nik", "Emma", "Gabi", "Gabriella", "Emily", "Parker", "Don", "Donna", "Linda", "Charles", "Charlie", "Lucas", "Donald", "Vennice", "Victoria", "Sebastian", "Sharon", "Tiffany", "Jay", "Elmer", "Mike", "Nathan", "Greg", "Alexis", "Alexander", "Aaron", "Adrian", "Andrew", "Aahana", "Adam", "Adison", "Alice", "Amari", "Angel", "Anthony", "Ava", "Aaliyah", "Aaradhya", "Abigail", "Achilles", "Amy", "Aimée", "Anders", "Archer", "Audrey", "August", "Bob", "Benjamin", "Bixby", "Brian", "Blake", "Birtha", "Brandon", "Billy", "Bill", "Bobby", "Carol", "Candice", "Cindy", "Cynthia", "Dewy", "Dustin", "Drake", "Eric", "Eden", "Emmma", "Emily", "Siouxsie", "Liam", "Noah", "Oliver", "Olivia", "Amelia"

# LAST NAME GENERATOR
LASTNAMES = "Phillips", "Bowden", "Valentine", "Brown", "Jackson", "Henson", "Johnson", "Patel", "Silva", "Wang", "O'Conner", "Henderson", "Smith", "Perkins", "Thompson", "Rose", "Clem", "Pruett", "Sears", "Maxine", "Evelyn", "Gonzales"

SEX = "Female", "Male"

# GENDER GENERATOR
GENDERS = "Agender", "Genderfluid", "Bigender", "Transgender", "Nonbinary", "Pangender", "Demigender", "Demiboy", "Genderqueer", "Androgynous", "Female", "Male"

PRONOUNS = "She/Her/Hers", "He/Him/His", "They/them/theirs", "Xe/xem/xyrs", "Ze/zir/zirs"

# JOB GENERATOR
JOBS = "Engineer", "Electrician", "Entertainer", "Factory Worker", "Chef", "Programmer", "IT", "Security Researcher", "Musician", "Film Producer", "Film Director", "Author", "Court Judge", "Lawyer", "Server", "NOJOB"

WEAPONS = "Colt Single Action Army Revolver", "AK-47", "M16 Rifle", "Brass Knuckles", "Scythe"


# NUMBER GENERATOR
NUM = "1", "2", "3", "4", "5", "6", "7", "8", "9"

# NUMBER GENERATOR
NUM2 = "3", "4", "5", "6", "7"

# NUMBER GENERATOR
NUM3 = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"

# PROGRAMMING LANGUAGES
PL = "A#", "A-0", "A+", "ABAP", "ABC", "ACC", "Accent", "Action!", "ActionScript", "Actor", "Ada", "Adenine", "AdvPL", "Agda", "Agilent VEE", "Agora", "AIMMS", "Aldor", "Alef", "ALF", "ALGOL 58", "ALGOL 60", "ALGOL 68", "ALGOL W", "Alice ML", "Alma-0", "Ambient Talk", "Amiga E", "AMPL", "Analitik", "AngelScript", "Apache Pig Latin", "Apex", "APL", "MIT App Inventor", "AppleScript", "APT", "Arc", "ArkTS", "ARexx", "Argus", "ASM", "AssemblyScript", "ATS", "AutoHotkey", "AutoIt", "AutoLISP", "Averest", "AWK", "Axum", "C", "C++", "C#", "Objective-C", "Javascript", "Ruby", "Python", "Brainfuck", 

# LOG
# added more hair 10/25/25

# HAIRSTYLES GENERATOR
HAIRSTYLES = "Mohawk", "Wolf Cut", "Bowl Cut", "Skullet", "Chelsea Cut", "Long Layered Cut", "Bob Cut", "Mullet", "Bixie", "Afro", "Buzz Cut", "Bouffant", "Broccoli Haircut", "Bunches", "Butch Cut", "Caesar Cut", "Chonmage", "Comb Over", "Conk", "Crew Cut", "Curtained Hair", "Dido Flip", "Ducktail", "Edgar Cut", "Eton Crop", "Fauxhawk", "Flattop", "French Crop", "Frosted Tips", "Hi-top Fade", "High and Tight", "Induction Cut", "Ivy League", "Marcel Waves", "Mop-top", "Pageboy", "Pixie Cut", "Pompadour", "Quiff", "The Seven", "Shape-up", "Skin Fade", "Slicked-back", "Titus Cut", "Tonsure", "Two Block", "Undercut", "Waves", "Wings", "Beehive", "Bangs", "Blowout", "Big Hair", "Brush Cut", "Bun", "Chignon", "Croydon Facelift", "Crown Braid", "Double Buns", "Devilock", "Fallera Hairdo", "Flipped-up Ends", "Feathered Hair", "Fontange", "French Braid", "French Twist", "Fringe (bangs)", "Half Crown", "Half Updo", "Hime Cut", "Jewfro", "Jheri Curl", "Lauered Hair", "Liberty Spikes", "Lob", "Odango", "Oseledets", "Payot", "Perm", "Pigtails", "Ponyhawk", "Ponytail", "Psychobilly Wedge", "Queue", "The Rachel", "Rattail", "Razor Cut", "Ringlets", "Shag Cut", "Shingle Bob", "Step Cut", "Surfer Hair", "Tail on Back", "Updo", "Weave", "Asymmetric Cut", "Braid", "Cornrows", "Dreadlocks", "Extensions", "Finger Waves", "Fishtail Hair", "Highlights", "Natural"

# COLORS
COLORS = "Red", "Blue", "Yellow", "Green", "Orange", "Purple"

# STREET NAMES
STREETS = "Broadway Street", "Phillips Street", "Pine Street", "Pine Road"

# DIRECTIONS
DIRECTIONS = "North", "East", "South", "West"

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

# CHOOSE DIRECTION
direction = random.choice(DIRECTIONS)

# CHOOSE STREET NAME
streetname = random.choice(STREETS)

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

# CHOOSE SEX
sex = random.choice(SEX)

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

# GENERATE NUMBER (1)
num6 = random.randint(0, 1000)

# GENERATE NUMBER (2)
num7 = random.randint(100, 1000)

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

# CHOOSE E-CC-NUMBER
ECCN = random.randint(0, 9999)

os.system("clear")

# PRINT ART
print("""▄▖▖  ▖▄ ▄▖▄▖▖ ▖▖
▙▖▛▖▞▌▙▘▙▖▙▘▌ ▌▌
▙▖▌▝ ▌▙▘▙▖▌▌▙▖▐ 
                """)

# PRINT FIRST NAME
print("Your character's first name: " + fn)

# PRINT LAST NAME
print("Your character's last name: " + ln)

print(" ")

# PRINT HEIGHT
print(fn + "'s height: " + num3 + "'" + num4)

print(" ")

# PRINT SEX
print(fn + "'s sex: " + sex)

# PRINT GENDER
print(fn + "'s gender: " + gender)

# PRINT PRONOUNS
print(fn + "'s pronouns: " + pronouns)

# PRINT RELATION
print(fn + "'s relation: " + ft)

print(" ")

# PRINT ADDRESS
print(fn + "'s address: " + str(num7) + " " + direction + " " + streetname)

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

print(fn + "'s cash amount: $" + str(num6))
  
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

print(" ")

question = input("Save character? (y)es, or (n)o: ")

if question == "y":
  os.system("touch " + "E-CC-" + str(ECCN) + ".txt")
  with open('E-CC-' + str(ECCN) + '.txt', 'w') as f:
    f.write("""
▄▖▖  ▖▄ ▄▖▄▖▖ ▖▖
▙▖▛▖▞▌▙▘▙▖▙▘▌ ▌▌
▙▖▌▝ ▌▙▘▙▖▌▌▙▖▐ """ + "\n" + "\n" + "Your character's first name: " + fn + "\n" + "Your character's last name: " + ln + "\n" + "\n" + fn + "'s height: " + num3 + "'" + num4 + "\n" + "\n" + fn + "'s sex: " + sex + "\n" + fn + "'s gender: " + gender + "\n" + fn + "'s pronouns: " + pronouns + "\n" + fn + "'s relation: " + ft + "\n" + "\n" + fn + "'s address: " + str(num7) + " " + direction + " " + streetname + "\n" + "\n")

if(jb == "Programmer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(jb + "\n" + fn + "'s Programming Language: " + pl)
  
if (jb == "NOJOB"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have a job.")
  
if (jb != "NOJOB" and jb != "Programmer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s job: " + jb)

# PRINT YEARLY INCOME
if (jb == "Programmer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Engineer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Author"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")

if (jb == "Electrician"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Chef"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Security Researcher"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "IT"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2  + ",000")
  
if (jb == "Court Judge"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Musician"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Lawyer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Film Producer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Film Director"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + num3 + ",000")
  
if (jb == "Entertainer"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
  
if (jb == "Factory Worker"):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write("\n" + fn + "'s yearly salary: $" + num + num2 + ",000")
    
with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
  f.write("\n" + "\n" + fn + "'s cash amount: $" + str(num6) + "\n" + "\n")
  
if (lor8 == 1):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s weapon: " + weapons)
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have a weapon.")

with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
  f.write("\n" + "\n" + fn + "'s body hair percentage: " + percent + "%" + "\n" + fn + "'s hairstyle: " + ht + "\n" + fn + "'s hair color: " + COLORS[hc] + "\n" + fn + "'s left eye color: " + COLORS[lec] + "\n" + fn + "'s right eye color: " + COLORS[rec] + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s left armpit hair color: " + COLORS[lahcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any left armpit hair." + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s right armpit hair  color: " + COLORS[rahcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any right armpit hair." + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s chest hair color: " + COLORS[chcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any chest hair." + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s stomach hair color: " + COLORS[shcolor] + "\n")
else:
    with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
      f.write(fn + " does not have any stomach hair." + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s back hair color: " + COLORS[bhcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any back hair" + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s left leg hair color: " + COLORS[llhcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any left leg hair." + "\n")

if (bhpercentage > 50):
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + "'s right leg hair color: " + COLORS[rlhcolor] + "\n")
else:
  with open ('E-CC-' + str(ECCN) + '.txt', 'a') as f:
    f.write(fn + " does not have any right leg hair." + "\n")