# START

       # Exercise 1

height: float = float(input('Enter your height: '))

while height < 0.4 or height > 2.5:
    print("Wrong input!!!")
    height: float = float(input('Enter your height: '))
else:
    print(f"Your height is {height}!")

       # Exercise 2

x: int = int(input('Enter the 1st number'))
y: int = int(input('Enter the 2nd number'))

if x > y:
    for a in range(y, x + 1):
        print(a, end=" ")
else:
    for a in range(x, y + 1):
        print(a, end=" ")
print()

       # Exercise 3

pi: float = float(input('Enter the equivalent of pi: '))
counter: int = 1

while pi != 3.14 and counter < 3:
    counter += 1
    print("Wrong!!! Try again")
    pi: float = float(input('Enter the equivalent of pi: '))

if pi == 3.14:
    print("You're right congregation!!!")
else:
    print("You are Wrong!!! The answer is 3.14")

        # Exercise 4

print(f"Enter three numbers 1st need to be between 1 to 10, second between 10 and 60 and the third number 60 and 100! ")

while True:
    num1: int = int(input("Enter the 1st number: "))
    num2: int = int(input("Enter the 2nd number: "))
    num3: int = int(input("Enter the 3rd number: "))
    is_valid_num1 = 0 < num1 < 11
    is_valid_num2 = 10 <= num2 <= 60
    is_valid_num3 = 60 <= num3 <= 100
    avg_num = (num1 + num2 + num3) / 3 == num2
    if is_valid_num1 and is_valid_num2 and is_valid_num3 and avg_num:
        print(num1, num2, num3)
        break

         # Exercise 5

legal_age: int = 18
beer = 10

for x in range(1, 10 + 1):
    your_age: int = int(input('Enter your age: '))
    if your_age >= legal_age:
        beer -= 1
        print('Here is your beer!!!')
        print(f"{beer} beers left")
    else:
        print('you are too young! here take a juice...')

# END
