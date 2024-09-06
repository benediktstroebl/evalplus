```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted(enumerrange(len(numbers))): numbers[x]]

# Test case 1: [1, 2, 3]
result1 = rolling_max([1, 2, 3])
assert len(result1) == 4
assert result1 == [1, 2, 3, 3]

# Test case 2: [1, 2, 4, 3]
result2 = rolling_max([1, 2, 4, 3])
assert len(result2) == 4
assert result2 == [1, 2, 3, 4]

# Test case 3: [1, 2, 3, 4, 5]
result3 = rolling_max([1, 2, 3, 4, 5])
assert len(result3) == 5
assert result3 == [1, 2, 3, 4, 5]

# Test case 4: [1, 2, 6, 7, 8]
result4 = rolling_max([1, 2, 6, 7, 8])
assert len(result4) == 5
assert result4 == [1, 2, 6, 7]

# Test case 5: [2, 4, 6, 8, 3]
result5 = rolling_max([2, 4, 6, 8, 3])
assert len(result5) == 5
assert result5 == [2, 4, 6, 8]
```
The function `rolling_max` in this script accepts a list of integers as an input and outputs a list of rolling maximum elements from that list. This is tested by the method using the sorted list and the element index. The test cases are then included to validate the function's correctness.