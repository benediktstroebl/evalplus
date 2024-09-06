```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # Sort the list of numbers to ensure elements are in a non-decreasing order
    rolling_max = [x for x in numbers if x == numbers[-1]] + numbers[:-len(numbers) // 2]
    return rolling_max
numbers = [3, 2, 4, 1, 3]
result = rolling_max(numbers)
print(result)
```