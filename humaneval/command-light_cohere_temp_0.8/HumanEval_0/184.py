Here's the Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.4)
       a 0.5, 1.1e0, 0.0], 0.6)
   2, 0.5) are 0.3), 0.6 are 0.8), 0.9, 0.2) False
   0.0, 0.0]
   0.4, 0.5, 0.0, 0.1, 0.0, 0.8), True
   0.4 is 0.1), 0.5, 0.8, 0.5, 0.2, 0.0, 0.0], 0.4, 0.0, 0.0, 0.0]) -> True if any? rolled numbers are close to each other, then there is a False returned. If we pass the same threshold, we will return True if there are any two numbers that are less than our threshold and are next to each other.