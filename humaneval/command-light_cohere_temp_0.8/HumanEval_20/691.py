Here's a solution to the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).

    Parameters:
    numbers: List[float] - A list of numbers.

    Returns:
    (smallest, largest) numbers in the list.
    """
    return (sorted(numbers, key=lambda x: (-x, -abs(x)))[0], -1)[0]
```