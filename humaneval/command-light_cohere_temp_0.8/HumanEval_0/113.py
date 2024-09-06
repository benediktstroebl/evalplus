```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)""" False
   rolled for=[1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.3] to haverolled_for each other.
    # Use this if numbers are sorted and the two numbers to compare are close, return True
    if the difference is smaller than the threshold
    # return True
    else return False
    # return False

# Test
print(has_close_elements([1.0,2.0,3.0,4.0,4.0,5.0, 0.0, 4.0, 1.2, 0.0, 3.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0])```