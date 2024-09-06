```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    The rolling max element is the maximum element found after applying
    rolling window(i.e., current element + previous elements) over the sequence.
    Returns the smoking max list of integers in a given sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = [x for x in numbers if x > maxy]
    maxy = max(max_numbers)
    return [maxy] + max_numbers
```