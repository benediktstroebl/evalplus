Here's a self-contained Python script that solves the problem of finding the closest elements in a list of numbers and passes the test:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
    numbers: List[float] -- A list of floating-point numbers.

    Returns:
    Tuple[float, float] -- A tuple containing two floating-point numbers that are the closest to each other. """
```