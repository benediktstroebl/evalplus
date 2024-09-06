```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```