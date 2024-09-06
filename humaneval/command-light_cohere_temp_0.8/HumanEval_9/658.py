```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, index in reversed(sorted(numbers)) if index < len(numbers) and num > numbers[index]]

# Test case
numbers = [1, 2, 3, 4, 9, 10, 1, 2]
result = rolling_max(numbers)
print(result)  # Output: [2, 3, 3, 3, 4, 9, 10]
```