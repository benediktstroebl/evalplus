```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    max_index = 0
    for i, num in enumerate(numbers[1:]):
        if num > max_number:
            max_number = num
            max_index = i+1
    return [max_number, max_index]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3]
```