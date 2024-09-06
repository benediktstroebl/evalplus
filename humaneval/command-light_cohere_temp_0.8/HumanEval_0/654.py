```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5) isOK. True
   
    has_close_elements([1.0, 2.0, 3.0], 0.9)
   Read True
    perfect pair.")
    return True
    """

This function takes a list of numbers as input and a threshold as a parameter. It uses the `hasclose` function from the built-in module `collections` to check if any two elements in the list are closer than the threshold.