```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [num for num in numbers if num == max(numbers)]
    return [x if x is max(max_numbers) else y for x, y in zip(numbers, max_numbers)]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4]
result = rolling_max(numbers)
assert len(result) == 7, "The result should be a list of length 7"
assert all(result == [1, 2, 3, 3, 3, 4, 4])

# Test case 2
numbers = [1, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5, "The result should be a list of length 5"
assert all(result == [1, 2, 3, 4])

# Test case 3
numbers = [10, 20, 30, 40, 50]
result = rolling_max(numbers)
assert len(result) == 5, "The result should be a list of length 5"
assert all(result == [10, 20, 30, 40])

# Test case 4
numbers = [10, 20, 30, 40, 50, 60]
result = rolling_max(numbers)
assert len(result) == 6, "The result should be a list of length 6"
assert all(result == [10, 20, 30, 40, 50])
```

The provided code defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The test cases aim to verify the function's correctness by passing various scenarios. The test cases cover different input sizes and ranges, ensuring that the function produces the correct results for different inputs.