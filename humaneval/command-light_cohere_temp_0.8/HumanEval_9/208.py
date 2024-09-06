```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    Parameters:
    numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of rolling maximum elements found until the given moment in the sequence.
    """
    list comprehension and a rolling window is created by taking every k-th element in the sequence and checking if this element is larger than the rolling maximum found so far (i. The rolling maximum is updated with each element, and the initial element is set to the first element in the list.
# The rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as an input and returns a list of the rolling maximum elements found until the given moment in the sequence. The function uses a list comprehension and a rolling window approach to solve the problem.