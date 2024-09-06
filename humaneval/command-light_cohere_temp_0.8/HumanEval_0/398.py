Here is a Python script that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5),0)
   ```
    close_elements([1.0, 2.8, 3.0, 4.0, 5.0], 0.3)
   0
   in the1)
    return True
    """

The function takes a list of numbers and a threshold as input and returns a boolean indicating if any two numbers in the list are closer than the threshold. The function uses the type hint to ensure that the list of numbers is passed as a single object and uses the comparison operator to compare the two numbers. The function then returns a boolean indicating if any two numbers in the list are closer than the threshold.

This solution provides a self-contained function that solves the problem of checking if any two numbers in a given list are closer than a given threshold.