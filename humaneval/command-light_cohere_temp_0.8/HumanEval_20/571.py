```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two numbers with the smallest and largest values, respectively.
    """
    values = sorted(numbers, reverse=True)  # Sort the list in descending order
    first = values[0]  # Get the smallest value in the list
    last = values[-1]  # Get the largest value in the list
    # Return the two values that are the closest to each other
    return Tuple(first, last)
```