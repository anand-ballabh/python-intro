# What is a function
# Defining a function
def func():
    print("Anand")
# Calling afunction
func()

# Function parameters and arguments
def nameprinter(name):
    print(name)

nameprinter("Samridh")

# Return
def givename(name):
    return name

abc = givename("Shlok")

print(abc)

def power(base, exp):
    x = 1
    for i in range(1, exp+1):
        x = x * base
    return x
y = power(4,2)
print(y)

# Recursion

