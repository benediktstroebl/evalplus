```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x > max(numbers[:-len(numbers) - 1])]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [4, 5, 1, 6]
result = rolling_max(numbers)
print(result)

numbers = [2, 3, 1]
result = rolling_max(numbers)
print(result)
```
The code defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the maximum element from the original list after each element has been rolled one position. The test cases demonstrate the time this function for different input lists, and the output is printed to the console.