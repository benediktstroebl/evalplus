```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
    - numbers: List[float] - A list of floating-point numbers.
    Returns:
    - A tuple of two floating-point numbers that are the closest to each other. """

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
two closest numbers that are found, with the first being (2.0) and the second being (3.2).0). Both numbers numbers closest numbers are returned in order, with the smaller number, larger number.

Note that this function assumes that the input list contains at least two elements. If it doesn't, a ValueError will be raised.