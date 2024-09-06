Certainly! Here's a self-contained Python function that sorts and validates a list of numbers in markdown code format:
```python
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    numbers = numbers.split()
    
    # Validate input
    numbers is a list of strings
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Convert each string to int and sort
    numbers.sort()

    # Convert the Mind numbers to integers
    numbers = [int(num) for num in numbers]

    return numbers.sort().
```
This function takes a string of numbers separated by spaces as input, validates that it contains a list of numbers, converts the string into a list of numbers, sorts the list, and returns the sorted list as a string.