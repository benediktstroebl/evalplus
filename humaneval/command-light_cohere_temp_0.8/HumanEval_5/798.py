```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * len(numbers))]

# Test the function with a list of numbers and a delimiter
test_data = [4, 2, 8, 3, 1]
test_delimiter = 4

result = intersperse(test_data, test_delimiter)
assert result == [4, 8, 2, 8, 3, 8, 1]
assert result == [4, 4, 2, 4, 3, 4, 1]
assert result == [4, 2, 8, 8, 8, 3, 8]
```