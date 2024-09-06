Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers, and returns a string with the numbers sorted from smallest to largest.
    >>> numbers = [3, 1, 5]
    >>> sorted_str = sort_numbers(numbers)
    ['one', 'three', 'five']
    """
    return [str(num) for num in sorted(numbers, reverse=True)]
```