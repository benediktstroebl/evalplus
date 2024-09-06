```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers. Sort the list of numbers and return a sorted string
    """
    numbers = [int(x) for x in numbers.list(str.split())]
    dry_run!is a list comprehension that goes through the string and converts each character to its integer equivalent. Then, it uses the list(numbers) to sort the numbers and returns the sorted string.