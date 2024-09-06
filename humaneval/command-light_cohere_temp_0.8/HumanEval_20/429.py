```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # find two elements with the smallest and largest values respectively
    smallest = largest = float('inf')
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    if smallest == largest:
        return (smallest, largest)
    return None
```