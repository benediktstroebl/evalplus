```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)?Drastic and the supports test.
    < numbers in numbers, then any two numbers are considered as close if their Euclidean distance is less than the given threshold.
    return bool"""