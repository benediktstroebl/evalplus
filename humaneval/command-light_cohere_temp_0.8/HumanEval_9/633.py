```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in the given list of integers.
    Each element in the
    list will be visited for the first time, then the rolling maximum will be updated and
    returned for each subsequent call.
    """
    elements: List[int]
    Returns: List[int]
    """
    rolling_max_element = []
    for num in numbers:
        rolling_max_element.append(max(rolling_max_element, num))
    return rolling_max_element
```