```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Test suite
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    "Test 1: Should return 1, 3, 4",
    "Test 2: Should return [1, 3, 4]",
    "Test 3: Should return []",
    "Test 4: Empty list",
]
result = remove_duplicates(numbers)

print("Result:", result)
for test, expected in test_remove_duplicates:
    print(f"Test {test}:\t{expected}")
```