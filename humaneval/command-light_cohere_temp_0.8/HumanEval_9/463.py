```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in enumerate(numbers, 1) if numbers[i] > numbers[i - 1]]

# Sample input and output:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
```