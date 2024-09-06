```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(num for num in numbers if num >= 0)
    return [max(max_numbers) for max_numbers in max_numbers]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```