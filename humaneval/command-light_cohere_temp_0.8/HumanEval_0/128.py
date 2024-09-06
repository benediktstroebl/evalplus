Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.6)
   /**
   uncho

    
This function will first convert the input list to a set and then check for any two numbers that are less than the threshold and that are also in the set. The function returns true if the set contains any two elements that satisfy this condition, otherwise it returns false.