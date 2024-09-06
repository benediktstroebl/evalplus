Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   2.

    None

return False

Given a list of numbers and a threshold, the function checks if there are any two numbers in the list that are closer than the threshold. The function returns True if any two numbers are closer than the threshold, and False otherwise.