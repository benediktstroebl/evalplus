```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.copy(numbers, return [num for num in numbers for num in numbers if num > numbers[-1]])

numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function called `rolling_max`, which takes a list of integers as input and generates a new list with the maximum integers from the original list, effectively rolling over the maximum elements in the list. This is similar to the test if the function can correctly solve the problem of finding the maximum elements in a list, given that the function works as expected.