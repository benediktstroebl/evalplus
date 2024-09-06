```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(sorted(numbers), range(len(numbers))) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Test case 1
numbers = [1, 2, 3, 4, 5]
print(rolling_max(numbers))  # [1, 2, 3, 3, 4, 5]

# Test case 2
numbers = [0, 1, 2, 3, 4, 5]
print(rolling_max(numbers))  # [1, 2, 3, 4, 5]

# Test case 3
numbers = [1, 0, 2, 3, 4]
print(rolling_max(numbers))  # [1, 2, 3, 4]

# Test case 4
numbers = [1, 2, 3, 4, 3, 2, 1, 5]
print(rolling_max(numbers))  # [1, 2, 3, 4]
```

This Python function, `rolling_max`, takes a list of integers as input and returns a new list containing the rolling maximum elements. The function uses the this sorted list and then iterates through it using a zip operation, comparing each element with the previous one. The rolling maximum element is found by selecting the element that is greater than its predecessor.