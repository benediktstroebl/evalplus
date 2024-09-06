```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects two numbers from the list that are the closest to each other and returns them in order (smaller number, larger number)
    :type numbers: List[float] -> Tuple[float, float]
    numbers = sorted(numbers, key=lambda x: (-x, x)))
    return numbers[0], numbers[1]
```