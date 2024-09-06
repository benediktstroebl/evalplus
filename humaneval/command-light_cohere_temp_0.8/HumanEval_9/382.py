```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x > max(numbers[:-len(numbers) + 1])]

# Test case 1: Single number list
single_number_list = [1]
result = rolling_max(single_number_list)
assert len(result) == 1
assert result[0] == 1

# Test case 2: List of numbers
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5
assert result[0] == 1
assert result[1] == 2
assert result[2] == 3
assert result[3] == 3
assert result[4] == 4

# Test case 3: Range-limited list
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers[:2] + [4, 5])
assert len(result) == 3
assert result[0] == 1
assert result[1] == 2

# Test case 4: Duplicate value in list
numbers = [1, 2, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5
assert result[0] == 1
assert result[1] == 2

# Test case 5: Sorted list
numbers = [3, 2, 1, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5
assert result[0] == 1

# Test case 6: Empty list
numbers = []
result = rolling_max(numbers)
assert len(result) == 0
```