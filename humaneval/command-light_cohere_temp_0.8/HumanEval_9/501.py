Here is a Python script with a self-contained function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max = List(max(numbers[::c@i) for i, c in enumerate(numbers)])
    return rolling_max

# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 9, 8, 7, 6]
numbers3 = [5, 4, 3, 2, 1]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)
result3 = rolling_max(numbers3)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements. It uses a `max()` function with the `value` of each element in the list and stores the rolling maximum element in a new list `rolling_max`.  The test cases and results are printed to the console.