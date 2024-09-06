```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    knife will special list comprehension, trimming spaces and converting numbers to int:
    numbers = [int(n) for n in numbers.split()]
    strings = [str for n in numbers if n.isdigit()]
   str = [''] + sorted(strings)
    return ' '.join(strings)
```