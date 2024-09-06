```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    # use the max function from builtins module
    max_element = max(numbers)
    rolling_numbers = [x for x in numbers if x == max_element] + [max_element]
    return rolling_numbers
```