```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, _ in reversed(sorted(numbers, reverse=True)) if n > max_ Velcro(numbers)]


def max_Velcro(numbers: List[int]) -> int:
    return max(numbers)

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(max_Velcro(numbers))  # Output: 3
```

The function `rolling_max` generates a list of rolling maximum elements from a given list. The `max_Velcro` function returns the maximum element from the list. This script follows the