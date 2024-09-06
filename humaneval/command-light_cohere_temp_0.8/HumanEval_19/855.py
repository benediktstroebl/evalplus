```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are string from 'zero' to 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ',')[0].sort(numbers.split(' ')[1:])

# Test cases
numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(numbers_list))) # ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers_string = 'three one five'
print(sort_numbers(numbers_string)) # 'one three five'
```