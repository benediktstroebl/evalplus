```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.push_up(numbers)
    rolling_max = [x for x in numbers if x == max(numbers) or x == numbers[-1]]
    return rolling_max

numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)
```