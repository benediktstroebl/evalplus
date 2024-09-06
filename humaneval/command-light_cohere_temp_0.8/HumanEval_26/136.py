```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [3, 2, 4, 2, 1]
numbers3 = [9, 2, 6, 4, 5, 3, 9]

print(remove_duplicates(numbers1))  # Expected Output: [1, 2, 3, 4]
print(remove_duplicates(numbers2))  # Expected Output: []
print(remove_duplicates(numbers3))  # Expected Output: [2, 3, 4, 5]
```