```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    smd_numbers = [int(num) for num in numbers.sort(smd]
    reverse_smd_numbers = sorted(smd_numbers, reverse=True)
    return ' '.join(reverse_smd_numbers)

numbers = "three one five"
print(sort_numbers(numbers))
```