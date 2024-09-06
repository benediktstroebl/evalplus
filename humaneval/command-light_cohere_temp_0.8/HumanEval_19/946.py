```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
   IO(numbers)
    numbers = [int(x) for x in numbers]
    numbers.sort()
    strings = ['zero','one','two','three','four','five','six','seven','eight','nine']
    return numbers.join(str.join(sorted(numbers, str))
```