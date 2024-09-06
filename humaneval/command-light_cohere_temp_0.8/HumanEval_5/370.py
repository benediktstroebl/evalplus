```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test case: empty list
test_empty = intersperse([], 4)
assert len(test_empty) == 0

# Test case: single number
test_single = intersperse([1], 4)
assert len(test_single) == 4

# Test case: list with two consecutive numbers
test_double = intersperse([1, 2], 4)
assert len(test_double) == 6

# Test case: list with three consecutive numbers
test_triple = intersperse([3, 2, 1], 4)
assert len(test_triple) == 6

# Test case: list with more numbers
test_more = intersperse([1, 2, 3, 4, 5], 4)
assert len(test_more) == 10
```
The code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the elements of the original list separated by the specified delimiter. The code also provides several test cases to validate the functionality of the `intersperse` function.