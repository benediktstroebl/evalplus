```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0.0, 2.0, 3.2.0])
   5> recheck the=True, because all the numbers are bigger than the threshold
    """
    return True

# Test the function with sample input
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0]
has_close_elements(numbers, 0.2)

print(has_close_elements(numbers, 0.2))
```