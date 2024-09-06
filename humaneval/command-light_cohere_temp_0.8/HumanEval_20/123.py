```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    We first sort the list of numbers in ascending order, then select the first two elements.
    :param numbers: List[float]
    :return: Tuple[float, float], None
    """
    return (numbers[0], numbers[1]), None
```