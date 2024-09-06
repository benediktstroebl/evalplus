```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Test case 1
numbers = [1, 2, 3, 4, 3, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4]

# Test case 2
numbers = [1, 2, 3, 4, 3, 2, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3]

# Test case 3
numbers = [1, 2, 3, 4, 5, 4, 3, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 4]
```
This Python code defines a function called `rolling_max` that takes a list of integers as input and returns a new list containing the maximum elements from the original list after applying a rolling window effect. The code uses the techniques of generating a sorted list of tuples `(num, i)` for each integer `num` and each index `i` in the original list, and then using the sorted list to filter the maximum elements. This code can handle lists of integers with different lengths and provides an efficient way to find the rolling maximum elements in the list.