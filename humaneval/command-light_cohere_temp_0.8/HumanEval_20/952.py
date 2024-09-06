```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Return a tuple containing the two elements in the list that are closest to each other.
    """
    list_sort_key=lambda x: -x)  # Sort the list in descending order
    x = numbers[0]
    while len(numbers) >= 2 and numbers[1] - x < 1e-6:
        x = numbers[1]
    return (x, y)
```