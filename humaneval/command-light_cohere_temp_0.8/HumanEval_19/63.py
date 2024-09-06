Here is a Python script that contains a self-contained function that sorts a list of numbers in ascending order:
```python
# Function to sort list of numbers in ascending order
def sort_numbers(numbers: str) -> str:
    # Split the input string into a list of numbers
    numbers = numbers.split()
    number = [int(i) for i in range(0, 10)]
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    # Join the sorted list back into a string
    return ' '.join(sorted_numbers)

# Test cases
test_cases = [
    "three one five",
    "zero one three",
    "two three four",
    "one eight six",
    "seven nine"
]

# Function calls
sorted_text = sort_numbers(test_cases)
print("Sorted text:", sorted_text)
``` 
The script defines a function **sort_numbers** that takes a string of numbers as input and returns a sorted string of those numbers. The test cases provide a input for the function, which should return the expected output, and the output is then printed to the console.