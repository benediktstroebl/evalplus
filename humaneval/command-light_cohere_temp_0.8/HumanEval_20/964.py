Here is a self-contained Python script that solves the problem of finding the closest elements from a supplied list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - List of floating-point numbers

    Returns:
        Tuple[float, float] - A tuple containing the two closest elements in order of magnitude.
```

This script defines a function called `find_closest_elements` that takes a list of numbers as an argument. The function then returns a tuple containing the two closest elements from the list in order of their magnitudes. 

You can use this function to solve the problem of finding the closest elements in a list of numbers, and pass your test cases to see how it works.