```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:]+[delimeter])]

# Test cases
test_numbers = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # Expected output: [1, 4, 2, 4, 3]
test_list = [1, 2, 3, 4, 5]
test_result = intersperse(test_list, 3)
print(test_result)  # Expected output: [1, 4, 5, 8, 12]
```