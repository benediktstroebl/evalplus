```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sum()
     # This max_elt = float('-inf')
    current_max = num
    for num in numbers:
        if num > current_max:
            current_max = num
        elif num == current_max and num < max_elt:
            max_elt = current_max
    return [current_max]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```