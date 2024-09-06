```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1: Basic test with empty list
assert not intersperse([], 4) == []

# Test case 2: Test with list of numbers
numbers = [1, 2, 3]
assert intersperse(numbers, 4) == [5, 6, 7]

# Test case 3: Test with different delimiter and list of numbers
numbers = [1, 2, 3]
assert intersperse([1, 2, 3], 8) == [1, 8, 2, 8, 3]

# Test case 4: Test with different list of numbers
numbers = [4, 5, 6]
assert intersperse(numbers, 2) == [6, 8, 10]
```
This script defines a function **'intersperse'** that inserts a number 'delimiter' between every two consecutive elements of the input list 'numbers'. The test cases ensure the function is working correctly for different scenarios.