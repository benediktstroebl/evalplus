Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two distinct elements are closer than threshold, False otherwise.
    for n in numbers:
        for m in numbers:
            if abs(n - m) < threshold:
                return True
    return False
```
This function takes a list of numbers and a threshold as input and returns True if any two distinct elements in the list are closer than the threshold, and False otherwise.