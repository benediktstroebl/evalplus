```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i % 2 == 0 and num > numbers[i]]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
print("Test 1: ", rolling_max(numbers))  # [1, 2, 3, 3, 3, 4]

numbers = [1, 2, 3, 2, 3, 4, 2, 3]
print("Test 2: ", rolling_max(numbers))  # [2, 3, 3, 3, 4]

numbers = [1, 3, 4, 2, 5]
print("Test 3: ", rolling_max(numbers))  # [1, 3, 4]

numbers = [10, 20, 30, 40]
print("Test 4: ", rolling_max(numbers))  # [30, 40]
```
This Python code defines a function `rolling_max` that takes a list of integers as input and generates a new list of integers, where each element is the maximum of the current element and all preceding elements. The code also includes several test cases to verify the correctness of the `rolling_max` function.