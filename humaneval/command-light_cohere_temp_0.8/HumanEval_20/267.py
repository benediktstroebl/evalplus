```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements in the list that are closest to each other. The function returns a list of two floats with the smallest number first, as required.
"""
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

min_distances, max_distances = tuple(map(lambda x: math.abs(x - y) for x, y in numbers)),
    return (numbers[min_distances], numbers[max_distances])
```