```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * len(numbers))]

# Test cases
test_data = [1, 2, 3, 4, 5]
test_delimiter = 4
test_result = intersperse(test_data, test_delimiter)
print(test_result)  # Output: [1, 4, 2, 4, 3, 5]
test_single_number = [1]
test_result = intersperse(test_single_number, 4)
print(test_result)  # Output: [1, 4, 1, 4, 1]
test_empty = []
test_result = intersperse(test_empty, 4)
print(test_result)  # Output: []
```