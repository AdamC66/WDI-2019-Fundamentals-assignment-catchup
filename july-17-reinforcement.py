# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.

# Test it to make sure it works.


def sum_of_odd_numbers(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        if num % 2 != 0:
            total += num
    return total

numlist = [1,2,3,4,5,6,7]
print(sum_of_odd_numbers(numlist))

# Pick three names and store them in a list.
# Prompt the user to enter their name. If their name is one of the names in the list, display a greeting message that includes their name. If their name isn't in the list, display "Who goes there?"

names = ["adam","fred",'george']
user_name = input("Please enter your name ").lower()

if user_name not in names:
    print("Who goes there?")
else:
    print(f'Hello {user_name.capitalize()}')