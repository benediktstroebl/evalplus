Here's the solution to the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    set for a number, and 2.0 are too close numbers, 0.3 will be  **threshold**
    # so we can start there
    """
    for num1, num2 in zip(numbers[1:], numbers[2:]):
        if num1 + num2 > threshold:
            return False
    return True