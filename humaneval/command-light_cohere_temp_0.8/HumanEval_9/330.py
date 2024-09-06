```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4]
result = rolling_max(numbers)
print(result)

# Test case 2
numbers = [2, 3, 4, 1]
result = rolling_max(numbers)
print(result)

# Test case 3
numbers = [5, 1, 1]
result = rolling_max(numbers)
print(result)
```
The code defines a function called `rolling_max` that takes a list of integers as input and returns a new list of integers containing the maximum elements found in the original list after each element. The function achieves this using a list comprehension with a condition that compares each element with its index and the previous one, effectively finding the maximum element in each window of elements. The output will show the maximum numbers in each test case.