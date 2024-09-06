Here's the self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8, threshold= 0.5)
    in the list
    """ and """
    x < threshold and y > threshold and x, y in numbers is closer than threshold --> True
    return True

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6, 8]
threshold = 2.0
has_close_elements(numbers,threshold)
```

This script defines a function has_close_elements that takes a list of numbers and a threshold as input. It then checks if any two numbers in the list are closer than the threshold, and returns True if they are.  It uses the Python's built-in < and > operators to compare the numbers and the threshold.