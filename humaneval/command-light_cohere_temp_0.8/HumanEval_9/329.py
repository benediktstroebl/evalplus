Here's the solution:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of the rolling maximum elements in the given list
    """
    result = [num for num, index in enumerate(sorted(numbers)) if numbers[index] > num]
    return result
```