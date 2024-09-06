Here is a self-contained Python function that solves the problem and passes the corresponding tests:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```
This function takes two parameters: numbers: a list of float values and threshold: a float. It returns True. The following condition is true if in the given list of numbers, any two numbers are closer to each other than the given threshold.