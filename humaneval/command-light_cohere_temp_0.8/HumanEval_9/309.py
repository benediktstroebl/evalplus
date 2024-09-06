```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_value = numbers[0]
    current_value = numbers[0]

    for num in numbers[1:]:
        current_value = max(num, current_value)
        max_value = max(max_value, current_value)

    return [max_value]
```
The script defines a function `rolling_max` that calculates the rolling maximum element in a given list of integers. It initializes the unique rolling start with the first element of the list and then iterates through the rest of the elements, comparing them with the current maximum value. The rolling maximum is a a list that contains the updated maximum value at each step.