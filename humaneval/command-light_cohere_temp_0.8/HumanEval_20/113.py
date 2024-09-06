```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest elements in the list, and the order of the larger number.
    """
    two = sorted(numbers, key=lambda x: x[0]))
    a, b = map(lambda x: x[1], zip(numbers, [2] + [0] * (len(numbers) - 1) // 2)))
    return a, b
```