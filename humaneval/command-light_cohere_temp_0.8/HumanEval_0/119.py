```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
    particular
    same two numbers that have a smaller difference than the threshold

    Returns:
    True if there are any two numbers with a difference smaller than the threshold, else False.
    }