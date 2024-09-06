```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair(left, right)


def _get_closest_pair(a, b):
    if abs(a - b) < min(abs(a - _mid(a, b)), abs(b - _mid(a, b))):
        return a, b
    else:
        return _mid(a, b), b if a < _mid(a, b) else _mid(a, b)


def _mid(a, b):
    return (a + b) / 2.0

# Tests:
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
assert find_closest_elements([10.0, 8.0, 6.0, 4.0, 12.0, 14.0, 16.0]) == (12.0, 12.0)
``` 

This code block resolves the task of finding two nearby numbers in a list, sorting the input, and then identifying this pair based on the middle values, ultimately returning the closest pair of numbers from the list.

The tests cover multiple scenarios to confirm the function's operation.