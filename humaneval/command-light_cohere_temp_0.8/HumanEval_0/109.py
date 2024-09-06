Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    threshold = float(threshold)
    return any(abs(n1 - n2) <= threshold for n1, n2 in zip(numbers))
```
This function takes two arguments: numbers, which is a list of float numbers to be checked, and threshold, which is the minimum distance between two numbers in the list that need to be closer than. The function returns true if there are any two numbers in the list that are closer than each other than the given threshold.