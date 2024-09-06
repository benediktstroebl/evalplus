```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_list = [num for num in numbers if num > max_element]
    max_element = max(max_list)
    return [max_element]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```