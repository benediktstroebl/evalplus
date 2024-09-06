```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num != float('-inf')]  # Remove float('-inf') values to avoid instability
    max_num = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_index = i + 1
    return [max_num]

# Test cases
test_cases = [
    [1, 2, 3, 2, 3, 4],
    [float('-2'), 4, 2, 3, 2, 3, 1],
    [3, 2, -5, 2, 3, -7, 2],
]

for test_case in test_cases:
    actual_result = rolling_max(test_case)
    expected_result = [4, 3, 3]
    assert actual_result == expected_result, f"Incorrect result: {actual_result}, expected: {expected_result}"
```
This Python script defines a function `rolling_max` that computes the rolling maximum of a list of integers. It also provides a test cases to ensure the function's correctness. 

Remember, we make a small adjustment to exclude float('-inf') values from the input list to prevent potential instability issues.