```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements in a given list of integers.
    The list comprehension will the rolling maximum elements, and returns the list.
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    max_elements = [x for x in numbers if x > numbers[0]]
    return max_elements
```