```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.1)
   2
    have numbers that are close, and the threshold value
    is less than the absolute difference between them.
    Return: True if any number in the list is closer to another than the threshold,
    return: False
    """
    for n1, n2 in zip(numbers, numbers[1:]):
        if abs(n1 - n2) < threshold:
            return True
    return False
```

This script defines a function called `has_close_elements` that checks if any two numbers in the given list are closer to each other than a given threshold. The function iterates through pairs of elements in the list, and if any pair meets the condition, it returns True. Otherwise, it returns False.