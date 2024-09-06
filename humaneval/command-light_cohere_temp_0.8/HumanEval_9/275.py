```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumerrange(len(numbers)), key=lambda x: numbers[x], reverse=True)]

# Test cases for rolling_max function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "List should have 7 elements"
assert sorted(result) == [1, 2, 3, 3, 3, 4, 4] , "Order should be correct"

numbers = [4, 4, 4, 4]
result = rolling_max(numbers)
assert len(result) == 4, "List should have 4 elements"
assert sorted(result) == [4, 4, 4] , "Order should be correct"

numbers = [0, 1, 2, 3]
result = rolling_max(numbers)
assert len(result) == 3, "List should have 3 elements"
assert sorted(result) == [0, 1, 2] , "Order should be correct"
```