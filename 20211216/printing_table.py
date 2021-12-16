x = int(input("enter a number "))
if (x % 2) == 0:
    print("Given number is even")
else:
    print("Given number is odd number")

for i in range (1,11):
    #print(str(x) + "x" + str(i) + "=" + str(x * i) )
    print(f"{x} X {i} = {x*i}")

# Variable Naming
# snake case: samridh_anand_paatni
# Camel Case: samridhAnandPaatni
# Pascal case: SamridhAnandPaatni
# Shouting snake case: SAMRIDH_ANAND_PAATNI

# conventions:
# constant: CAPITALS
# normal variables: small
# classes, objects: Firstcapital