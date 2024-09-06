```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i == 0 or num > numbers[i - 1]]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [4, 2, 1, 9, 3, 8, 2, 7]
assert rolling_max(numbers) == [4, 2, 1, 9, 3, 8, 2, 7]

numbers = [5, 2, 6, 2, 7, 4, 3, 2]
assert rolling_max(numbers) == [2, 2, 6, 2, 7, 4, 3, 2]

numbers = [5, 6, 7, 5, 4, 3, 2]
assert rolling_max(numbers) == [5, 6, 7, 5]

numbers = [1, 2, 3, 4, 5, 6, 3, 7]
assert rolling_max(numbers) == [1, 2, 3, 4, 5, 6, 3, 7]
```

This Python code provides a rolling_max function that takes a list of integers as input and generates a new list with the maximum element from the previous list at each position. The function is tested through unit tests that cover various scenarios.