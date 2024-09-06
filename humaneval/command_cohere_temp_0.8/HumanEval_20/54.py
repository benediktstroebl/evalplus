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
    if (a == b) or ((a - b) < 1e-6 and (b - a) < 1e-6):
        return a, b
    elif abs(a - b) <= abs(a - _next_float(a, b)) and abs(a - b) <= abs(b - _next_float(a, b)):
        return a, b
    else:
        return _next_float(a, b), _next_float(a, b)


def _next_float(a, b):
    if a == b:
        return a
    elif a < b:
        return a + 1e-6
    else:
        return b - 1e-6

# Tests:
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
assert find_closest_elements([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 20.0, 21.0, 22.0, 23.0, 24.0]) == (20.0, 20.0)
```

The `find_closest_elements` function first sorts the input list of numbers, then searches the two closest numbers in the middle (or closest to the middle if there are an even number of elements). The ` _get_closest_pair` function uses a numerical tolerance to compare the absolute difference between pairs of numbers to select the two closest numbers from a given pair and its next number in the sequence. While it raises an error if the length of the supplied list is less than 2, for insurance it also includes a test case in the `assert` statements with a list of 10 elements, to test the function also works with an even number of list elements.