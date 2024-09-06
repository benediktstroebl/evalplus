```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num > 0]  # Filter out negative numbers
    max_index = numbers.max_num = max(numbers)
    rolling_maxes = [num for i, num in enumerate(numbers) if num == max_num]
    return rolling_maxes
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```