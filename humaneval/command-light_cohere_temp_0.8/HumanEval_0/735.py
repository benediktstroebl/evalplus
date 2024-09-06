Here is a self-contained Python script with a function that solves the problem of checking if any two elements in a list are closer than a given threshold:

```python
from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any( math.abs(num1 -num2 -threshold) < math.abs(numbers[0]) and numbers[0] != threshold and has_close_elements(numbers[1:], threshold)
    return False
```
This function takes a list of numbers and a threshold as input and returns a boolean indicating whether any two elements in the list are closer than the threshold. The function uses the absolute value calculation to determine if two elements are close enough, and then checks if the first element is not equal to the threshold.

The function will return True if any two numbers in the list are closer than the threshold, and will return False otherwise.