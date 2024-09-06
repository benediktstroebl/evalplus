```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.2) is
    right.0, 0.8, 3.0, 4.0, 5.0, 6.0, 7, 8, 9) [threshold=1]
    has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6], 0.3)
   0.8, 6.3, 3, 8, 7.0, 6, 5, 9, 10,11]
    """