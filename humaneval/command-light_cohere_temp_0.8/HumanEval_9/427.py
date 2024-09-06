```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        elif num == max_num and max_count < len(numbers) - 1:
            max_count += 1
    return [max_num for _ in range(max_count)]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```