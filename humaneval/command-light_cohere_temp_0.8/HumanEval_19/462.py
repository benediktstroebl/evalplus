Below is a Python script with a self-contained function that solves the problem of sorting numbers in a markdown code block:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine. Valid choices are
    numbers are 'zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Create a list of numbers from the input string
    numbers = [int(num) for num in numbers.
    # Sort the final list of numbers in ascending order
    numbers.sort()
    numbers
    numbers
    return ''.join(numbers)
```
This script defines a function `sort_numbers` that takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. It uses the list comprehension and the built-in `sorted` function to achieve this. 

Please note that the function assumes that the input contains only numbers from zero to nine, and it will raise an error if the input contains invalid characters or non-numeric values.