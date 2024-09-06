```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest elements from the list of numbers, and returns them in order of the smaller number."""
    a, b = sorted((a, b) for a, b in zip(numbers, numbers[1:]))
    return a, b
```