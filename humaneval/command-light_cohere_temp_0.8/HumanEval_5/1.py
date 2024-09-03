```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [1, 2, 3, 4, 5]
test_delimiter = 4
test_results = intersperse(test_data, test_delimiter)
print(test_results)  # Expected output: [0, 4, 6, 8, 10, 12]

test_single_number = [1]
test_delimiter = 4
test_results = intersperse(test_single_number, test_delimiter)
print(test_results)  # Expected output: [1, 4, 8]

test_empty_list = []
test_delimiter = 4
test_results = intersperse(test_empty_list, test_delimiter)
print(test_results)  # Expected output: []
```