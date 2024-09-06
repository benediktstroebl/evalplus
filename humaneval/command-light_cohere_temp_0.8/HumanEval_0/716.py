Here is a self-contained Python script that solves the problem of checking if any two numbers in a list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
    open and5
    open the list of numbers)

    For any two numbers in the list, if they are within the given threshold of each other, then they are considered close.

    The function returns True if any two numbers in the list are close to each other and returns False otherwise.