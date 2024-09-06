Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
   return a tuple with the two closest elements.
    """


numbers: List[float]

Returns: Tuple[float, float]

Example usage:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)
```