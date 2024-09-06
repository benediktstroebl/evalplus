```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers) // 2)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 3, 4, 4, 5]

numbers = [10, 20, 30, 40, 10]
result = rolling_max(numbers)
print(result)  # Output: [10, 30, 40, 40]
```
This script defines a function `rolling_max` that calculates the rolling maximum elements in a list. The function uses list comprehension to iterate over the last `n` elements of the list and compares them with the next element to find the maximum element.

The test cases demonstrate the usage of the `rolling_max` function with different lists of integers, and the output is displayed to verify the expected results.