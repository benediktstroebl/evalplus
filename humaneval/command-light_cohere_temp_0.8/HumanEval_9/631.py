```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling maximum elements in the given list of integers.
    """
    list of numbers is passed to the function
    """
    return [num for num in numbers for _ in numbers if _ == max(numbers)]
```