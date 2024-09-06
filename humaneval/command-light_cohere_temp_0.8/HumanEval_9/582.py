```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_value = numbers[0]
    current = max_value
    for num in numbers[1:]:
        current = max(num, current)
    return [current]
# Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```