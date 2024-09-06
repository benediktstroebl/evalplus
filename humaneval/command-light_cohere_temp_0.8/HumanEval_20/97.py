```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects two closest elements and returns them in order (smaller number, larger number) """
    # Sort the list of numbers
    numbers.sort(sorted(numbers, key=lambda x: x))
    # Take first two elements from the sorted list
    first, second = numbers[0], numbers[1]
    # Return both elements in order, with smaller number first
    return Tuple(first, second)
```