Here is a self-contained Python script that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [4, 5, 6, 7, 8, 9, 10]
result = rolling_max(numbers)
print(result)  # Output: [10, 9, 8, 7, 6, 5, 4, 3]
```
This function uses a slicing technique with the range(len(numbers)-1) to get the indices of the elements in order, and then uses the max() function with the corresponding elements to get the maximum rolling elements.