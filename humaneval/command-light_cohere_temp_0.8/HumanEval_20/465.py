```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects two elements that are closest to each other from the supplied list and returns them in order (smaller number, larger number)
    """
    if len(numbers) < 2:
        return (None, None)

    min_val, max_val = (float('inf'), -float('inf'))
    for num in numbers:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    return (min_val, max_val)
```