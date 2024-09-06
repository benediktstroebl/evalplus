Here is a Python script that contains a self-contained function to solve the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
   media impossible.

    This if len(numbers) < 2 or threshold > numbers[0] - numbers[-1]
        return False
    """

This function works by using the Python function `len` to check if the list of numbers has less than 2 items. Then it checks if the the threshold is greater than the difference between the last and the first number in the list. This ensures that the numbers in the list are in increasing order.