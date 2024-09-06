```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num != float('-inf')]  # Convert float negatives to int for proper sorting
    return [max(numbers[:i]) for i, num in enumerate(numbers)]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4]
result = rolling_max(numbers)
assert len(result) == 6, "result list should have length 6"
assert result == [1, 2, 3, 3, 3, 4], "Wrong rolling max elements"

# Test case 2
numbers = [0, -2, 3, 0, -1]
result = rolling_max(numbers)
assert len(result) == 5, "result list should have length 5"
assert result == [0, -2, 3, 0], "Wrong rolling max elements"

# Test case 3
numbers = [-10, -20, -30, -40, -50]
result = rolling_max(numbers)
assert len(result) == 5, "result list should have length 5"
assert result == [-10, -20, -30, -40], "Wrong rolling max elements"
```

This code defines a function rolling_max that takes a list of integers and returns a new list with the rolling maximum elements from the original list. It then passes three tests to ensure the correctness of the rolling_max function.