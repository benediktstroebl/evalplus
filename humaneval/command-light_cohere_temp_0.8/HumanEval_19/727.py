```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ``` 
This script defines a function sort_numbers that takes a string of numbers delimited by spaces and sorts it. The function uses a list comprehension to convert each number into an integer, and then sorts the list of integers using the sorted() function. 

The resulting sorted numbers are then joined back into the original string with spaces.