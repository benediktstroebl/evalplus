```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split().
    numbers.split(',') 
    new :
        numbers.split(',') 
    numbers = [int(n) for n in numbers]
    sorted(numbers)
    return ''.join numbers.sorted()
 numbers.

numbers = 'three one five six seven eight nine'
print(sort_numbers(numbers))
```