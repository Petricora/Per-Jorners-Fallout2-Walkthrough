# Lesson 42:
# for i in range(1, 13):
# 	print(f"No. {i} squared is {i ** 2}, and cubed is {i ** 3}")
# print("*" * 80)


# Lesson 43:
name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))
print(f"{name} is {age} years old.")

if age == 900:
    print("Sorry, Yoda, you died in the 'The Return of the Jedi'.")
elif age >= 18:
    print(f"You're old enough to vote, {name}.")
    print("Please ensure to put an 'X' in only one box.")
else:
    print(f"You're not old enough to vote; please come back in {18 - age} years.")
