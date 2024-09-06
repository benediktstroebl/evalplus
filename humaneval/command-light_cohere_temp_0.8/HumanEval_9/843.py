```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_list = [num for num in numbers if num > max nook]
    return [max(max_list)]

# Test case 1
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5, "Error: Wrong length"
assert result[0] == 5, "Error: First element is not maximum"

# Test case 2
numbers = [1, 1, 2, 3]
result = rolling_max(numbers)
assert len(result) == 3, "Error: Wrong length"
assert result[0] == 3, "Error: First element is not maximum"

# Test case 3
numbers = [2, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5, "Error: Wrong length"
assert result[0] == 5, "Error: First element is not maximum"

# Test case 4
numbers = [3, 4, 5, 6, 7]
result = rolling_max(numbers)
assert len(result) == 7, "Error: Wrong length"
assert result[0] == 7, "Error: First element is not maximum"
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list with the maximum elements after each moment. It also has a test cases to verify the functionality of the function.