Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0.1)
   1 is not possible pass threshold, but are closer to each other than
    0.9
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0]) -> True
   0
   5)
    return True
else:
    return False
```
The function takes two parameters: numbers: a list of float numbers, and threshold: a float. When the function is called, it will return True if it's possible to add two numbers in numbers and the sum of these numbers is less than or equal to the threshold, otherwise, it will return False.