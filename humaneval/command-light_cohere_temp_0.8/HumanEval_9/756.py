```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "Error: Function did not return the correct list length"
assert result == [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [5,1,1]
result = rolling_max(numbers)
assert len(result) == 3, "Error: Function did not return the correct list length"
assert result == [5,1,1]
```