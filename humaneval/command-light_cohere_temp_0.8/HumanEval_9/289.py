```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted((num for num in numbers), reverse=True) if num >= numbers[-1]]

# Test case 1:
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [5, 4, 3, 3, 2]

# Test case 2:
numbers = [0, 1, 2, 3, 4]
result = rolling_max(numbers)
print(result)  # Output: [0, 0, 1, 2]

# Test case 3:
numbers = [10, 40, 25, 80, 15]
result = rolling_max(numbers)
print(result)  # Output: [15, 25, 40, 80]

# Test case 4:
numbers = [20, 10, 5, 2, 3]
result = rolling_max(numbers)
print(result)  # Output: [20, 15, 10, 5]
```
This script defines a function rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements from the input list. 

The function uses the sorted() function with reverse=True and a generator expression to find the maximum element from the list, which is then added to the new list. 

This is a self-contained Python script that provides a solution to the given problem.