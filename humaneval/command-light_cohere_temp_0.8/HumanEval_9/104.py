```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max and num != numbers[0]:
            # Update the current_max when equal to a smaller number but not the starting number
            current_max = num
    return [current_max]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```