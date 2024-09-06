```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num >= 0]  # Remove negative numbers
    return [max(numbers[i:], max(numbers[:i+1])) for i in range(len(numbers))]

# Test case 1: Remove negative numbers from [1, 2, 3, -100]
numbers = [1, 2, 3, -100]
result = rolling_max(numbers)
assert all([1, 2, 3, 100]) == result

# Test case 2: Remove negative numbers from [1, -2, 3, 4, 5]
numbers = [1, -2, 3, 4, 5]
result = rolling_max(numbers)
assert all([1, 2, 3, 4, 5]) == result

# Test case 3: Remove negative numbers from [10, -3, 7]
numbers = [10, -3, 7]
result = rolling_max(numbers)
assert all([10, 3, 7]) == result
```
The function `rolling_max` takes a list of integers as input and returns a list of the rolling maximum elements in the sequence. The function uses slicing to calculate the maximum element for each sublist of the sequence and returns the final list of rolling maximum elements.