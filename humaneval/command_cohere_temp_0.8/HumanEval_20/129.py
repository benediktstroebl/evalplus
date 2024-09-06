```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    return numbers[0], numbers[-1] if delta == 0 else numbers[0] + delta / 2.0

# Tests:
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 22.0]) == (20.0, 22.0)

test_find_closest_elements()
``` 

This script sorts a list of numbers, then checks for the smallest delta between the first and last numbers in the list; thereafter, it returns either the first and the last number or the first number and that same number incremented by half of the delta. The tests check the function's behavior for different input lists.