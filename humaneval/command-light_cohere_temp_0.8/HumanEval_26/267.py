```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


# Test suite
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

numbers = [4, 4, 1, 2]
result = remove_duplicates(numbers)
print(result)

numbers = [3, 2, 1]
result = remove_duplicates(numbers)
print(result)
```