```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A list of integers is given, along with a start index and moment.
    Calculate the Rolling Maximum element using the simple math and return the maximum number.
    """
    list comprehension is used to generate the list of rolling maximum elements, where the maximum element is taken from the list starting from the moment of the start index.
    return: [max_number, max_number + 1, ..., max_number + n]
    """
    return [max(numbers[i:i + 1]) for i in range(start_index, len(numbers), 1)]
```