```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]


# Test suite:
numbers = [1, 2, 3, 2, 4]
print("Test 1:", remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [1, 3, 2, 4, 2]
print("Test 2:", remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 2, 4, 5]
print("Test 3:", remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [10, 10, 10]
print("Test 4:", remove_duplicates(numbers))  # Expected output: []
```