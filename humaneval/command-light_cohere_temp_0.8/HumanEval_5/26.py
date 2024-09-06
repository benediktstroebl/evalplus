```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+j for i,j in zip(numbers, numbers[1:]+[delimeter])]

# Test
test_numbers = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # Expected output: [1, 4, 2, 4, 3]

test_lists = [[1, 2, 3], [4, 5], [6, 7]]
test_delimiters = [4, 8]
test_results = map(intersperse, test_lists, test_delimiters)
print(test_results)   # Expected output: [[1, 12, 2, 12, 3], [16, 20], [28, 28]]
```