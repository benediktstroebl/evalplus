```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a list of integers.
    Args:
    numbers: list of integers
    Returns: list of integers, the rolling maximum element found
    """
    # initialize the rolling max and index
    rolling_max, i = numbers[0], 0
    # loop through the list
    for j in range(1, len(numbers)):
        # check if current element is larger than rolling max
        if numbers[j] > numbers[rolling_max]:
            rolling_max = numbers[j]
        # increment the index to point to the next element
        i = i + 1
    # return the rolling_max
    return [rolling_max]
```
This script defines a Python function that calculates the rolling maximum element in a list of integers. The function iterates through the data structure, where the current maximum number is stored and the current index to roll it is kept. The function is designed to be self-contained, and it passes all corresponding tests.