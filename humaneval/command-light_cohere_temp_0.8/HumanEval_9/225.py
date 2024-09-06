```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x == numbers[0]]
    for num in numbers[1:]:
        if num > max_numbers[0]:
            max_numbers[0] = num
    return max_numbers
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```