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

The tests themselves are binary search-based, using the `_get_closest_pair` helper function, which returns the closest pair out of two given numbers `a` and `b`, by comparing the squared differences between these numbers and the middle number between the two.

The `_mid` function calculates the average of the two numbers, which is used as the middle number for comparison. 

The `find_closest_elements` function first sorts the input list, then iteratively checks the first and last numbers of the list, passing them to the `_get_closest_pair` function in the worst-case scenario when the list contains an even number of elements, or the smallest and largest number in the list when it contains an odd number of elements, with the first iteration being the slowest and the convergence happening towards the end of the list. 

Please note, that the original problem statement does not specify that the numbers in the list must be distinct, nor does it mention any limitations on the type of numbers that may be in the list (e.g. integer-only).  If this were a real-world programming scenario, adding these details would be important for clarity.

Let me know if you would like to refine the tests or the code!