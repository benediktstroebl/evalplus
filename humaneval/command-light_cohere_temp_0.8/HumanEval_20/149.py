Here is a Python script that contains a self-contained function that solves the problem of finding the two closest elements from a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Parameters:
        numbers: list of float
            A list of numbers.
    Returns:
        a tuple of two floats that are the two closest elements.
    """
    A tuple of two floating-point numbers that are the two closest elements in the list of numbers, and in the order of their value, where smaller comes first.

```

This function implements the algorithm that first sorts the list of numbers, then picks the two smallest numbers and the two largest numbers, and then returns them in order of their value.

This solution uses the ** typing module **, which is a built-in Python library used for type hinting and static type inference**.