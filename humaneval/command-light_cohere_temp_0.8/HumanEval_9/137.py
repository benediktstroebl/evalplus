```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found until a given moment
    in the sequence. Using the provided list of integers.
    """ The time is to be performed in the order of numbers appearing in the list.
    """

    list of rolling maximum elements = [2, 3, 3, 4, 4, 5]
    """
    numbers.append(max(numbers[:-1]))  # rolling max update
    return numbers

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```