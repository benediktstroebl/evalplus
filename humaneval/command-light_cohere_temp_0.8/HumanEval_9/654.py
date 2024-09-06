```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.split = [list(numbers)
    max_num = numbers[0]
    current = max_num
    
    for num in numbers[1:]:
        current = max(current, num)
        max_num = max(current, max_num)
    
    return [max_num]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```