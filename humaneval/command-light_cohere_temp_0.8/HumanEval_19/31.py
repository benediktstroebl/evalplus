```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ``` 
The function takes a string of numbers in the format 'zero12345' and returns a string with the numbers sorted from smallest to largest.