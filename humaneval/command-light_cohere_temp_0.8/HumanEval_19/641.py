```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sorted()
 numbers = sorted(set(numbers.split()) 
    numbers = [int(num) for num in numbers]
    numbers = list(numbers) 
    return "".join(str(num) for num in numbers)
``` 
This function, named `sort_numbers`, takes a string of numbers separated by spaces as input and returns a string with the numbers sorted from smallest to largest. The function uses the numbers to be converted into a set, then sorts the set and converts it back into a string.