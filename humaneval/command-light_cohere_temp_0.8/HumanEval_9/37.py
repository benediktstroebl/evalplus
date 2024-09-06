```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment
    in the sequence.
    Test Case:
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> numbers = [4, 2, 1]
    >>> rolling_max(numbers)
    []
    """
    numbers.append(numbers[-1])
    return numbers[:-1] + [max(numbers)]
```
This function rolling_max takes a list of integers numbers as input and generates a list of the rolling maximum elements found until the given moment in the sequence. In this process, the maximum element in the current sequence is added to the back of the sequence, then the sequence is updated with the new maximum element. 
Finally, the updated sequence is returned.