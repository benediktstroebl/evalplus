```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    """
    list of rolling maximum elements is returned.
    """

    list comprehension is used to find the maximum element, and then the 
    maximum element is rolled over to the next index.
    """
    list of rolling maximum elements is returned.

Test cases:
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]

>>> rolling_max([5, 6, 7, 8, 9, 10])
[10, 9, 8, 7, 6, 5]

>>> rolling_max([3, 6, 5, 7, 9, 10, 3, 6])
[9, 10, 7, 9, 10]
```

The function `rolling_max` takes a list of integers as input and returns a list of the rolling maximum elements found in the input sequence until the given moment. It uses list comprehension and the to find the maximum element, and then the maximum element is rolled over to the next index.