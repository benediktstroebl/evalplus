```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5) is True
   and False
    """ > threshold"""
    return any(n1 <= n2 for n1, n2 in numbers) and n1, n2 in numbers < threshold)
``` 
This function works by iterating over the list of numbers and checking if any two numbers in the list are less than the given threshold.