```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num != float('inf')]  # Remove float('inf') to avoid infinity
    return [max(numbers[i:j]) for i, j in zip(numbers, numbers[1:]])
def test_rolling_max():
    return [rolling_max([1, 2, 3, 2, 3, 4, 2])]  # Should return [1, 2, 3, 3, 3, 3, 4, 4]
```