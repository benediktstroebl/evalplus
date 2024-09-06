```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    return numbers.split(' ')
    sns = [int(n) for n in numbers.
    return ' '.join(sorted(sns))

numbers = sort_numbers('three one five')
print(numbers)
```