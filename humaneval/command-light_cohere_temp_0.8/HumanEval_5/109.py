```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers, numbers[1:]) for j in numbers[1:] + [delimiter]]

# Test the function with an empty list
test_list = intersperse([], 4)
assert test_list == []

# Test the function with a list of numbers
test_list = intersperse([1, 2, 3], 4)
assert test_list == [1, 4, 2, 4, 3]

# Test the function with list of numbers and custom delimiter
test_list = intersperse([1, 2, 3], 100)
assert test_list == [101, 102, 103]
```