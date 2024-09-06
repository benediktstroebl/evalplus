```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements from the supplied list that are the closest to each other and returns them in order (smaller number, larger number). Returns a tuple of these two numbers"""
    if len(numbers) < 2:
        return (None, None)
    numbers.sort_by_descending() = sorted(numbers, key=lambda n: n)
    first, second = numbers[0], numbers[-1]
    return (first, second)
```