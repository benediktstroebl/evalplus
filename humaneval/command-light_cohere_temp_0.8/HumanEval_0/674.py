```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    if any(abs(n1 - n2) < threshold for n1, n2 in numbers):
        return True
    else:
        return False
```

This script defines a function called `has_close_elements` that checks whether any two elements in a given list of numbers are closer to each other than a given threshold. The function uses the Python's built-in `abs` function to compare the absolute values of two numbers and returns `True` if the condition is met, indicating that the two numbers are close enough. 
The function returns `False` otherwise, indicating that the list does not contain any close pairs.