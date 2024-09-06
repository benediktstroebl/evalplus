Here is a Python script that is self-contained and solves the problem you provided:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If there are any two numbers with difference less than the threshold, return True
    If there are no such pairs, return False
    """
    return any(x <= threshold for x in numbers[::index : len(numbers)])
```
The function `has_close_elements` takes a list of numbers and a threshold as input, and returns a boolean value indicating whether there are any two numbers in the list closer than the threshold. 

This function uses the Python list slicing to iterate through the list and uses the `<=` operator to check if any two numbers have a difference less than the threshold.