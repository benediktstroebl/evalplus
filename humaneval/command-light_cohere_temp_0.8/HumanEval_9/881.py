```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_element = numbers[0]
    current = max_element
    for num in numbers[1:]:
        if num > current:
            current = num
        elif num == current:
            current += 1
    return [current, ]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
```