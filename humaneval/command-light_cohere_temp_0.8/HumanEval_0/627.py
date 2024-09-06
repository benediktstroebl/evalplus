Here's the solution to the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0.5, 4.0, 5.0, 6.0, 8)
   3)
    # or any two numbers are closer than given threshold
    """
    return any(map(lambda x, y: x != y and x + y <= threshold, numbers))
```

This function takes two parameters: `numbers` (a list of floats), and `threshold` (a float). It returns `True` indicating if there are any two numbers in the list that are closer to each other than the given `threshold`.