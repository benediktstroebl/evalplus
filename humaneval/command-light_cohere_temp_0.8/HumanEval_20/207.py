```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other from the list of numbers
    supplied. Returns the two elements with the order (smaller, larger)
    """
    numbers = List(sorted(numbers))
    return (numbers[0], numbers[1])
```