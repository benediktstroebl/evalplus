```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and num >= numbers[i]]

# Tests
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # expected output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 3, 2, 4, 5]
result = rolling_max(numbers)
print(result)  # expected output: [1, 3, 3, 4, 4]

numbers = [9, 8, 7, 6, 5]
result = rolling_max(numbers)
print(result)  # expected output: [9, 8, 8, 7, 7]
```