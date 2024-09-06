```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_elements = [num for num in numbers if num > max_value]
    max_value = max(max_elements)
    
    return [max_value]

# Test case
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```