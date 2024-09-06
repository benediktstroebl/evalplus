```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_window = numbers[-1]
    rolling_max_list = [max_element for max_element in zip(numbers[:-], numbers[1:]) if max_element >= max_window]
    return rolling_max_list
```