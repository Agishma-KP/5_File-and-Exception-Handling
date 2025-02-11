# Exercise 1: Read and display file contents
with open(r"C:\Users\HP\Documents\Agiammu.txt", 'r') as file:
    content = file.read()
    print("Reading File Content:")
    print(content)

# Exercise 2: Copy file contents
try:
    with open(r"C:\Users\HP\Documents\Agiammu.txt", 'r') as source_file:
        content = source_file.read()
    with open(r"C:\Users\HP\Documents\Copy_Agiammu.txt", 'w') as destination_file:
        destination_file.write(content)

    print("File copied successfully!")

except FileNotFoundError:
    print("Source file not found.")

# Exercise 3: Count total number of words in a file
try:
    with open(r"C:\Users\HP\Documents\Agiammu.txt", 'r') as file:
        content = file.read()
        words = content.split()
        print("Total number of words in the file:", len(words))
except FileNotFoundError:
    print("File not found.")

# Exercise 4: Convert user input to an integer with exception handling
try:
    user_input = input("Enter a number: ")
    integer_value = int(float(user_input))
    print("Converted integer:", integer_value)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Exercise 5: Raise an exception for negative numbers in a list
try:
    numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))

    # Check for negative numbers
    if any(num < 0 for num in numbers):
        raise ValueError("Negative numbers are not allowed!")

    print("Valid list of integers:", numbers)

except ValueError as e:
    print("Error:", e)

# Exercise 6: Compute the average of a list of integers with exception handling
try:
    numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))
    average = sum(numbers) / len(numbers)
    print("Average of numbers:", average)
except ZeroDivisionError:
    print("Error: Cannot compute average of an empty list.")
except ValueError:
    print("Error: Please enter only valid integers.")
finally:
    print("Program execution completed.")

# Exercise 7: Write a string to a file with exception handling
try:
    filename = input("Enter the filename: ")
    content = input("Enter the content to write: ")
    with open(filename, 'w') as file:
        file.write(content)
    print("File written successfully! Welcome!")
except Exception as e:
    print("An error occurred:", e)







