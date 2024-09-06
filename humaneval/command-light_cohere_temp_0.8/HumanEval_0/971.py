Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5); 0.3)
    also be considered0 to each other than given threshold
    """
    # loop through all numbers
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```
This function checks if in a list of numbers, any two numbers are closer to each other than the given threshold.