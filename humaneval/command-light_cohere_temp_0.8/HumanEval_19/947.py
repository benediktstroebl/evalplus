```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    performers = []
    numbers[0]  # index of first number = 0
    numbers = [int(num) for num in numbers[1:]]
    for num in numbers:
        performers.append(str(f for f in 'abcdefghijklmnopqrstuvwxyz' if f < num))
    sorted_performers = ' '.join(performers)
    return sorted_performers
```