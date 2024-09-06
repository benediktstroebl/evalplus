Here is a Python script that solves the problem you have described:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two elements in the list are within the threshold, and False otherwise. """