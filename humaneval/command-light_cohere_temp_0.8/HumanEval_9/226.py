```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Calculate the rolling maximum element in a list of integers.
    """ 
    max_count = [0] * (len(numbers) + 1)
    for num in numbers:
        max_index = max_count[num == num] + 1 if num != numbers[-1] else len(numbers)
        max_count[max_index] += 1
    return [num for num, _ in enumerate(max_count) if _ == max_count[num]]
```