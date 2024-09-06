```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Use default ordered-insertion for sorting
    numbers.sort(numbers, key=lambda x: (-x, -x))
    return numbers[0], numbers[1]
```
This code provides a self-contained function that solves the problem of finding the closest elements in a list of numbers.