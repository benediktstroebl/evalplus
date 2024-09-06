```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [num for num in numbers if num == numbers[0]]
    for num in numbers[1:]:
        if num > max_numbers[0]:
            max_numbers[0] = num
    return max_numbers
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```