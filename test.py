print("Anand's first program. Courtesy Samridh ")
Name = "Anand"
print(Name)
##### Operators in Python ###
a = 7
b = 8
print(a + b)
print(a * b)
print(a - b)
print(a / b)

print(a ** b)
print(a // b)
print(a % b)

# decision making
x = int(input("enter physics marks "))
y = int(input("enter Maths Marks "))

if (x > 100 or x < 0) or y > 100 or y < 0:
    print("Please check input marks")
else:
# Individual subject analysis
    if x <= 50 and x >= 0:
        print ("Student is poor in Physics")
    elif x > 50 and x <= 70:
        print("Student is average in Physics")
    elif x >70 and x <=100:
        print("Student is very good in Physics")

    if y <= 50 and y >= 0:
        print ("And Student is poor in Maths")
    elif y > 50 and y <= 70:
        print("And Student is average in Maths")
    elif y >70 and y <=100:
        print("And Student is very good in Maths")

    # Subject comparision

    if x > y:       
        print("Comparing two subjects Student is better in Physics")
    elif x == y:
        print("Comparing two subjects Student is equally good in both Physics and Maths")
    else:
        print("Comparing two subjects Student is better in Maths")

# lists
names = ["Anand", "Samridh","Shlok", "Ruchi"]
professions = ["Job less", "Student","Student", "Teacher" ]
ages = [50, 19, 17, 43]
print(names, professions, ages)


# loops
# for loop
for name in names:
    print("Hello " + name + "!")

for i in range(4):
    print("Hello " + names[i] + " you are " + str(ages[i]) + " years old " + professions[i])
   
   
# while loop
for i in range(0, 10, 2):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 2 # i = i + 2

# i = i * 2 => i *= 2