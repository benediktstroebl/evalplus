```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and num >= numbers[i]]

# Unit Test
numbers = [1, 2, 3, 4, 3, 2, 1]
result = rolling_max(numbers)
assert len(result) == 7, "Error: Length should be 7"
assert result == [1, 2, 3, 3, 3, 4, 4], "Error: Result does not match"
print(result)
```