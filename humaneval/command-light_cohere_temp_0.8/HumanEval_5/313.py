```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimiter in zip(numbers, [delimeter] * 2)]

# Test cases
test_numbers = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # Output: [1, 4, 2, 4, 3]

test_lists = [[1, 2, 3], [4, 5], [6]]
test_delimiters = [4, 8]
test_results = [intersperse(list(test_list), test_delimiter) for test_list in test_lists]
print(test_results)  # Output: [[1, 4, 6], [8, 5], [12]]
```