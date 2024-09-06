```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, _ in sorted(enumerrange(1, len(numbers)+1), key=lambda x: numbers[x], reverse=True)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 3, 2, 4, 5]
print(rolling_max(numbers))  # [1, 3, 3, 4, 5]

numbers = [10, 20, 30, 40, 50]
print(rolling_max(numbers))  # [10, 20, 30, 40, 50]

numbers = [1, 2, 3, 4, 5, 6]
print(rolling_max(numbers))  # Error: ValueError
```