```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.8)
    0.000 count is
    right_close_elements_threshold = 0.05
    """
    count = numbers.count(threshold)
    if count > 1:
        return True
    else:
        return False
```