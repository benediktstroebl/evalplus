```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
    regional = numbers[0,3,4,5]
    numbers = [int(num) for num in numbers]
    return numbers[-1] if len(numbers)==1 else numbers[-2:]split(' ') + sorted(numbers[:-2])
```