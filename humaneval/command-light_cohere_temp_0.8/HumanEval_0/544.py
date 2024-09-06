```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.1)
    TFalse 
    """.9999
    
    """ One float value in the given list and another float value are less than
    the given threshold, then it will return True. Otherwise, False.
    """ This important()
```
Test the function with different arguments:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.1)
 True

>>> has_close_elements([8.0, 2.0, 3.0], 0.1)
 False
```