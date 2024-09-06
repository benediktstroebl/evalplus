```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Test case 1
numbers = [4, 2, 6, 3]
result = intersperse(numbers, 4)
assert list(result) == [4, 8, 6, 8, 10, 12, 3]

# Test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 6, 8, 10, 3]

# Test case 3
numbers = [4, 2, 6, 3]
result = intersperse(numbers, 5)
assert list(result) == [4, 9, 11, 16, 13]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the numbers separated by that delimiter. The test cases demonstrate the multiple ways to use this function with different inputs and expect the output to be correct.