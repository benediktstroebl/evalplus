Here is a self-contained Python script that defines a function to solve the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0, 0.5)
   0.1eInvalidNumber>have_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 0.4, 0.8, 7.0, 0.0])
    return False

    check if the two numbers are in the list of numbers and are less than the threshold, return True
    otherwise, return False.