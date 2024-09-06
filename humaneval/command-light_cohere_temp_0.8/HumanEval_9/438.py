```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from the input list.
    """
    list comprehension with slice is used to extract the rolling elements until the current element becomes the max element.
    Return a list of all rolling max elements found so far.
    """
example usage:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4]
    """
    numbers = list(numbers)
    current_max = numbers[0]
    rolling_maxes = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maxes.append(current_max)
    return rolling_maxes
```