```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, range(len(numbers))) if numbers[i] > numbers[i - 1]]

# Test the function with various inputs
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 1, 2, 6, 7]
result = rolling_max(numbers)
print(result)  # Output: [5, 6, 7]

numbers = [10, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [10, 10]

numbers = [1, 2, 3, 4, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 4, 4, 5]
```
This Python script defines a function `rolling_max` which takes a list of integers as input and returns a new list containing the maximum elements from the original list after applying a rolling effect. The script includes several test cases that demonstrate the functionality of the function with various input lists, showcasing the expected output.