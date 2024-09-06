Here's a self-contained Python script that solves the problem of finding the closest elements from a supplied list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    These are the first and second closest elements returned.

    # Sorting thewo numbers based on a custom sorting key
    numbers.sort(key=lambda x: x[1] - x[0])
    # Select the first and second closest elements
    first, second = numbers[0], numbers[-1]
    return first, second
```
This solution uses the `typing` module to provide type hints for the function parameters and return values. It sorts the using numbers based on a custom sorting key, which is the difference between the second element and the first element of the list. The solution then selects the two closest elements and returns them in order.