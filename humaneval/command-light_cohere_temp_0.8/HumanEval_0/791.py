```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.6)
   0
   50
   4.05], 0.03)
   5
   1.0," 0.00
   1
   10.0, 4.5])
   2.5)
   2, 0.0), 0.00
       1.0})
   0: False
    return False

# Example Test:
print(has_close_elements([1.0, 2.10, 3.2, 0.0, 0.0, 0.2, 0.5, 0.2, 4.0, 0.0])
```