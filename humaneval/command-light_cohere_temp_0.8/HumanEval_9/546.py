```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max = [rolling_max(numbers), [rolling_max([2, 3, 4])[0], 3, 2, 1, 4, 3, 2, 3, 2, 1]])
print(test_rolling_max)
```