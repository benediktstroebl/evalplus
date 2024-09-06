Here's a self-contained Python script that solves the problem of checking if any two elements in the list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)  #?. Any2> values in the list should be within
    threshold of each other.  """