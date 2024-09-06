```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a given list of integers.
    Each element is selected as max until the moment arrives.
    Returns a xmax elements as a list.
    """
    def rolling_max(numbers: List[int]) -> List[int]:
        return [x for x in numbers if numbers.count(max(numbers)) == 1][0]
    return numbers
```