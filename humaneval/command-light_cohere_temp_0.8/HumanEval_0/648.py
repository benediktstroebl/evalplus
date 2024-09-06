Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
    is allowed
    are in a complete range.
    >>> has_close_elements([1.0, 2.8, 3.0, 4.8], 0.0) is allowed
    it not be considered
    """
    The function returns a boolean value based on the input. It uses the `List` and `threshold` types from the typing module to ensure the function works with both built-python and type-friendly objects.