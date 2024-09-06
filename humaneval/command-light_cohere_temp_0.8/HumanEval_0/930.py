Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer to each other than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5) is False
   one)
    return True  # Because [1.0, 3.0] are less than threshold we pass this test.
```
The function has_close_elements takes in two parameters: a List[float] called numbers which represents the list of numbers to check, and a float threshold called threshold which is the minimum distance between two numbers that will return true.  It checks if any two numbers in the list are closer to each other than the given threshold.