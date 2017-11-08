#Kanon11


def add(a,b):
    print("Adding {} + {}".format(a,b))
    return a+b

def subtract(a,b):
    print("Subtracting {} - {}".format(a,b))
    return a-b
def divide(a,b):
    print("Division of {} / {}".format(a,b))
    return a/b
def multiplication(a,b):
    print("Multiplication of {}*{}".format(a,b))
    return a*b
print("Let's do some math with just functions!")

age=add(30,5)
height = subtract(78,4)
weight = multiplication(90,2)
iq=divide(100,2)

print(f"Age: {age} weight: {weight} height: {height} iq: {iq}")

print("here is a puzzle.")

what=add(age,subtract(height,multiplication(weight,divide(iq,2))))
print(f"that becomes {what}, can you do it by your hand")

a=int(input("please enter your a:"))
b=int(input("please enterr your b:"))

print("now you can see the result of (a+b)^2=a^2+2ab+b^2==={}\n".format(multiplication(add(a,b),add(a,b))))


