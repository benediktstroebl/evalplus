Here is a self-contained Python function that solves the problem of checking if any two numbers in a list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5),0) 0.5) 1.0)
   -- both cases are less than given threshold.
    """
    True
    If the list contains any pair of numbers that are closer than the given threshold, then the function returns True. If not, it returns False.