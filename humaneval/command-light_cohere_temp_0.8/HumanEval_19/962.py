Here's the corrected self-contained Python script with a function that sorts numbers in a markdown code block:
```python
from typing import List

def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers, sorts them and returns a string of sorted numbers in markdown format
    >>> sort_numbers([3, 1, 5]) # [1, 3, 5]
    ['one', 'three', 'five']
    """
    numbers.sort()
    local

    new_numbers = []
    for num in numbers:
        new_numbers.append(str(num))
    return ' '.join(new_numbers)
```
This script defines a function that takes a list of integers and returns a list of strings in markdown format, which are the numbers sorted from smallest to largest. The function uses the `str()` to convert each integer to a string, and then appends each string to a new list, which is returned.