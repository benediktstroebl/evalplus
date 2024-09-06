```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with an empty list
test_empty_list = []
result = intersperse(test_empty_list, 3)
assert len(result) == 0

# Test the function with a list of numbers
test_list = [1, 2, 3, 4, 5]
result = intersperse(test_list, 3)
assert len(result) == 10

# Test the function with a custom delimiter
test_delimiter = [1, 2, 3]
result = intersperse(test_delimiter, 4)
assert len(result) == 6  # Should have 3 pairs of (1, 2), (2, 3), (1, 4)
```