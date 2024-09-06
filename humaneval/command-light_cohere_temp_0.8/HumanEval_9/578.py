```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment
    in the sequence.
    Args:
        numbers (List[int]): Input list of integers.
    Returns: a list of rolling maximum elements in order.
    """
    rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.sort()
    max = numbers[0]
    output = [max]
    for i in range(1, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        output.append(max)
        output.append(numbers[i])
    return output
```
This script defines a function rolling_max that takes a list of integers as input and returns a list of rolling maximum elements found in that list, until a given moment in the sequence. The script is using the typing module for type hints and also sorts the input list of numbers using the sort() function to determine the initial value of the rolling maximum element.