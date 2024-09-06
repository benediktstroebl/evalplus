```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment in the sequence
    :param numbers: list of integers
    :return: list of rolling max elements found in the sequence
    """
    return [num for num, i in sorted(numbers, reverse=True) for i in range(1, 10)]
```

This script provides a self-contained function `rolling_max` that calculates and returns a list of the rolling maximum elements from a given list of integers. The function utilizes the returning a list comprehension, which iterates through the list and calculates the maximum element at each moment. The sorted function is used to sort the list in reverse order to achieve the desired behavior.