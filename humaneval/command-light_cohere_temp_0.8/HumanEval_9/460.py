```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers) if i < numbers[i+1] or i > numbers[-1-i]]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```