```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(sorted(numbers))
    return [x for x in numbers if x == numbers[-1]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [5,1,2,3,4,5]
assert rolling_max(numbers) == [5]

numbers = [2,1,3,1,4,3,2,1]
assert rolling_max(numbers) == [1,3,1,4,3,2]

numbers = [2,3,3,4,5,6,7]
assert rolling_max(numbers) == [6]

numbers = [9,2,8,3,7,4,6]
assert rolling_max(numbers) == [9]

numbers = [1,1,1,1,1,1,1,1]
assert rolling_max([x for x in numbers if x]) == []
```