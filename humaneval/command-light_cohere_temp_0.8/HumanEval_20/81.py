```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest elements from the list, and returns them in order of their magnitude.

    Parameters:
    numbers (List[float]): List of numbers with at least two elements.
    Returns a0 (small, large) elements of the list in order of their magnitude.

    Returns:
    Tuple[float, float]: The two closest elements in order of their magnitude.

Test code:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])

(2.0, 1.0)
```