Here is a self-contained Python script that defines a function called `has_close_elements`, which checks if any two numbers in a given list are closer than a given threshold.

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(abs(x - y) < threshold for x, y in zip(numbers))

print(has_close_elements([1.0, 2.0, 3.0, 0.5, 4, 0.0, 0.0, 5], 0.3)) # True
7  # now has any two elements, which are close to each other

This solution is self-contained, and it does not require any external functions or modules.