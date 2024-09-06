```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.2)
    can 
    : return True
   
    : If any two numbers in numbers are closer than given threshold, we can safely return True.
    : return False
    None
```