```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0) 0.6)
   100, 1.0, 3.0, 5.0, 10
   0, 3.0, 4.0]
 0, threshold= 1.0).8, threshold = 4.0  # Yes_close_elements([1.0, 2.0, 3.0], 0.5)
   0.8, 0.1)
   05) 2, 3.0, 5.0, 10, 2, 9, 7, 1.0, 5)
    return True
```