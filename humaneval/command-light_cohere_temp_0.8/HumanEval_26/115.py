```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < len(numbers) and num not in numbers[:len(numbers)]]


# Unit tests for remove_duplicates function
numbers_list = [1, 2, 3, 2, 4, 2, 3, 5]
result = remove_duplicates(numbers_list)
test_result = [1, 2, 3, 4, 5]

print("Test Results:", result)
print("Expected Results:", test_result)

```