Here's the solution for your problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    if two numbers are less than threshold, return True
    elif all([abs(n1 - n2) > threshold for n1, n2 in numbers]) or 
        any([n in numbers]) == 0):
        return True
    else:
        return False
    ```
Do you need anything else to help you with writing code or debugging?