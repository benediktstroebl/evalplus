Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer to each other than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(abs(x - y) <= threshold for x, y in zip(numbers))
```
This function takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold.

The function uses the abs() function to calculate the absolute difference between two numbers, and then checks if the difference is less than or equal to the threshold.

The function then returns a boolean indicating whether any such pair of numbers exists in the list that satisfies the condition.

This is a self-contained function, and does not require any additional variables or functions to be defined.