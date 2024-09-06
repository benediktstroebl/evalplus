Here's a self-contained Python function that solves the problem you described:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(numbers)  # Create a mutable copy to ensure changes aren't lost
    max_number = numbers[0]  # Assume the first element is the max
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return [max_number]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 5, "Unexpected length"
assert result[0] == 1, "Wrong max value"
assert result[1] == 2, "Wrong max value"
assert result[2] == 3, "Wrong max value"
assert result[3] == 3, "Wrong max value"
assert result[4] == 4, "Wrong max value"

numbers = [1, 3, 7, 5, 4]
result = rolling_max(numbers)
assert len(result) == 5, "Unexpected length"
assert result[0] == 1, "Wrong max value"

```
This code defines a function `rolling_max` that takes a list of integers as input and generates a new list of the maximum elements after applying a rolling window function. It uses the provides a original list to ensure changes aren't lost and the max value is calculated correctly. The code includes test cases to validate the correctness of the `rolling_max` function.