Here's the solution for the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0) and 0.8, 3.0, 4.0, 5.0, 2.0, 3)

    False
    """ be True, meaning that all the numbers are far away from each other."""
    return all(numbers) <= threshold
```

This function takes in a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold.