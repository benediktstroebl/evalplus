```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers as input and returns a list 
    of the maximum elements found while moving through the sequence, starting 
    from the beginning and moving towards the end of the list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    max_elements = []
    while numbers:
        current_max = numbers[0]
        numbers.remove(current_max)
        max_elements.append(current_max)
        numbers = [n for n in numbers if n != current_max]
    return max_elements
```