```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Tests
numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # [1, 3, 4]
numbers = [4, 4, 4, 1]
print(remove_duplicates(numbers))  # [1, 4]
```