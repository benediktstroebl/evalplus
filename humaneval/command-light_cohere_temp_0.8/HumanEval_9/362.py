```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer(), reverse=True)]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "Result should be length 7"
assert list(result) == [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [5, 2, 3, 1]
result = rolling_max(numbers)
assert len(result) == 4, "Result should be length 4"
assert list(result) == [1, 2, 3]

# Test case 3
numbers = [10, 20, 30]
result = rolling_max(numbers)
assert len(result) == 3, "Result should be length 3"
assert list(result) == [10, 20, 30]
```

The provided code defines a function `rolling_max` that calculates the rolling maximum element in a given list of integers. It uses the `enumer()` to sort the list in descending order and then selects the maximum element from each sorted sublist. The test cases demonstrate the scenario where the function is invoked with various input lists, and the expected results are compared with the actual output to ensure the correctness of the rolling_max function.