```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max:
            pass  # Element is same as the previous, so no update.
    return [current_max] as result
    return result
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```