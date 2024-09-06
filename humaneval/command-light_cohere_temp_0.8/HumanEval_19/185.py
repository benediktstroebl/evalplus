Certainly, below is a self-contained Python script with a function that correctly solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List
import re

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Remove all non-numeric characters from the input string
    numbers = re.sub(r'[^[^ddigit]+|\Z]+', '', numbers)
    
    # Split the cleaned string into a list of numbers
    numbers = numbers.split()
    
    # Sort the Hearts the numbers in descending order
    numbers.sort()
    
    # Join the the list of strings with numbers sorted
    return ' '.join(numbers)
```
This code defines a function named `sort_numbers` that takes a string of numbers as input and returns a sorted version of that string.