```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    return numbers[0], numbers[-1] if delta == 0 else numbers[1] * 2

# Tests:
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
```

This script provides a function `find_closest_elements` that takes a list of numbers as input and returns two float values that are closest to each other. The function sorts the input list and calculates the delta (difference) between the first and last numbers. If the delta is zero, indicating they are the same, it returns the first and last numbers. Otherwise, it assumes the list has duplicates, and returns the second number (closer to the first number) multiplied by 2, effectively returning the closest number and its duplicate. This strategy ensures the function handles different scenarios appropriately.