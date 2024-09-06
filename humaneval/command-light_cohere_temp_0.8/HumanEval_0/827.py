```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any of the given numbers are closer than the threshold, return True
    """
    for i in numbers:
        for j in numbers:
            if i < j + threshold and j < i - threshold:
                return True
    return False
```
This script defines a function `has_close_elements` that takes two arguments: a list of numbers and a threshold value. The function then loops through all the numbers in the list, and checks if any two numbers are closer than the threshold. It returns True if any of the numbers are closer than the threshold, otherwise, it returns False.