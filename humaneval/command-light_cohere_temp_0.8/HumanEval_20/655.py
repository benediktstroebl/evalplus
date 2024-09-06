```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).
    Input: numbers: list of floats, at least 2 elements.
    Output: two floats, the two elements in the list that are the closest to each other.

Test cases:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2])
2.0, 1.0)

>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])([1.0, 1.0, 1.2])
2, 1.1.5)
2.2, 0.2, 0.2]

```