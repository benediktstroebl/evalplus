```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Selects and returns two elements that are the closest to each other in the supplied list of numbers
    """
    # Sort the list of numbers
    numbers.sort(key=lambda x: (-x, x))
    # Select the first two elements of the sorted list
    return Tuple(numbers[0], numbers[1])
```