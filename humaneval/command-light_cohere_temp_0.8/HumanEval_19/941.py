```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ``` 
This script defines a function `sort_numbers` that sorts a list of numbers in a string. Using the `sorted` function with a custom sorting order. 

The function takes a string of numbers and returns a new string where the numbers are sorted from smallest to largest.