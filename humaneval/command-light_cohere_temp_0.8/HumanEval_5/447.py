```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Test the function with different types and lengths
test_data = [10, 3, 4, 7, 5, 8, 9]
test_data_empty = []
test_data_large = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_test_data = intersperse(test_data, 3)
result_test_data_empty = intersperse(test_data_empty, 3)
result_test_data_large = intersperse(test_data_large, 1)

assert result_test_data == [13, 16, 11, 19, 12, 22, 15, 8, 21, 9]
assert result_test_data_empty == []
assert result_test_data_large == [12, 14, 16, 19, 22, 25, 28, 31]
```