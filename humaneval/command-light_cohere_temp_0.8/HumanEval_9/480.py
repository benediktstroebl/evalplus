```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers, reverse=True) if x >= numbers[0]] + [numbers[0]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [4, 4, 1, 2]
result = rolling_max(numbers)
print(result)

numbers = [5, 2, 2, 3, 1]
result = rolling_max(numbers)
print(result)

numbers = [5, 2, 2, 3, 3]
result = rolling_max(numbers)
print(result)
```
This Python code defines a function called `rolling_max` that takes a list of integers as input and generates a new list of integers, containing the maximum element from the original list after each element in the list has been seen. The code then provides several test cases to demonstrate the functionality of the `rolling_max` function.