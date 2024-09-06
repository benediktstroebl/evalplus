```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    lowest_set  = set()
    numbers = set(numbers.split())
    string = ''
    for num in numbers:
        if num.isdigit():
            set_add(num)
    for num in lowest_set:
        if num > 'seven':
            break
    for num in set_add:
        string += num + ' '
    return string.strip()
```