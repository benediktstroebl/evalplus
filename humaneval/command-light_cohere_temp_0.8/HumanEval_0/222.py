Here is a self-contained Python script that solves the problem of checking if any two elements in the list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5) isTrue. False
   
   05
   0, True
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.8], 0.8)  #.9999
                False

   6
   6, 1.5, 1.0, 1.0, 3.0, 4.0, 0.0, 0.3), False
   0, True
    >>> has_close_elements([1.0, 1.0, 1.0, 2.5, 4.8, 0.0, 0.8, 0.8, 0.10, 0.0, 1.0, 3.0, 1.0, 0.6, 2.0], 0.0),0] False),3, False
    """