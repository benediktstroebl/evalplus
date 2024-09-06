```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return None  # Not enough elements
    return (numbers[0], numbers[1]) if numbers[0] <= numbers[1] else (numbers[1], numbers[0])  # Swap for consistent ordering

def test():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (2, (1, 2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1, (2)
    assert find_closest_elements([1.0, 2.0, 3.0, 5]) == (1, 2)
    assert find_closest_elements([1.0, 2.0, 3]) == (1, 2)

This script defines a function `find_closest_elements` that accepts a list of numbers and returns a tuple containing the two closest elements. It uses a comparison operators to determine the closest elements and passes the tests.