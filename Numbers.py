#Ask user for input
print("Please enter 5 numbers.")

#Make list to hold numbers
numbers=[]

#Loop to collect 5 inputs
i = 0
while i < 5:
    try:
        # Read input from the user
        number = (int(input("Enter number: ")))
        numbers.append(number)
        i = i + 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Calculate
sum_list = sum(numbers)
average = sum(numbers) / len(numbers)

#Display results
numbers.sort()
print('You entered:', (numbers))
print(sorted(numbers[0:1]), 'is the smallest number in this list.')
print(sorted(numbers[(len(numbers)-1):len(numbers)]), 'is the largest number in this list.')
print((average), 'is the average of this list of numbers.')
