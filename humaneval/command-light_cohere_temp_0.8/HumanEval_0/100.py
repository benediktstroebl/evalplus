```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0, 0.0, 2.0, 4.8, 3.0, 5.0, 6.1, 2)
   0, 7.2, 8)
    << True
    """