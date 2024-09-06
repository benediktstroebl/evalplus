```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest values to None
    first, second = None, None
    # Sort the list of numbers based on the values of each pair
    numbers.sort(key=lambda x: (x, x))
    # Initialize the first and second closest values again
    first, second = sorted(numbers, key=lambda x: (x, x)), (second, first)
    # Return the first and second closest values
    return first, second
```