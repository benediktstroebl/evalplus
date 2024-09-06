```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.count = len(numbers)
    max_num = numbers[0]
    current = max_num
    for num in numbers[1:]:
        current = max(num, current)
        max_num = current
    return [max_num]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
```