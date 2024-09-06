Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer to each other than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5); 0.9) False
    class too is
 
    return True
    """

This function takes a list of numbers and a threshold as input and returns a boolean indicating if any two numbers in the list are closer to each other than the threshold.

You can test the function by passing a sample list and threshold and compare the output with the expected result (True in this case).