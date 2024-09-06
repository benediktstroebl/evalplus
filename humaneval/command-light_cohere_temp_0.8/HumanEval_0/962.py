Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers.sort()
    threshold)
    Check if any two elements in the list have a distance less than the threshold."""
    return all(abs(x - y) <= threshold for x, y in zip(numbers))
```
This function uses the all function with the map operator to check if any two elements in the list have a distance less than the threshold.

The function returns True if any two elements in the list have a distance less than the threshold, otherwise it returns False.