```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Numbers are sorted from smallest to largest.
    Return: 'one two three four five six seven eight nine'
    """
    # convert string of numbers into list
    numbers = numbers.split()
     # create a list of characters
    numbers = [int(char) for char in numbers]
    # sort the list
    numbers.sort()
    important_ order is the numbers in ascending order.
    # join the important to create a new string
    return ''.join out(numbers)
```