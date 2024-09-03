```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers are any two numbers closer to each other than
    the given threshold.
    """
    if len(numbers) < 2:
        return False

    sorted_nums = sorted(numbers)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i - 1] < threshold:
            return True
    return False
```