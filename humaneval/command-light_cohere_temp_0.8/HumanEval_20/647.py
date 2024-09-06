Here is the solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least 2) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    """
    numbers = sorted(numbers, key=lambda x: (-x, x))
    return numbers[0], numbers[1]
```

The script uses the sorted function with a custom key that returns the pair of numbers in descending order. The function then returns the required tuple with the two closest numbers.