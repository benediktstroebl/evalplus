```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string can be 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
    impact = []
    for num in numbers:
        if num not in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            raise ValueError(f'Invalid input! Choose a valid number between zero and nine.')
        else:
            impact.append(num)
    list_sort(impact) = sorted(impact)
    string = ' '.join(sorted(impact))
    return string
```