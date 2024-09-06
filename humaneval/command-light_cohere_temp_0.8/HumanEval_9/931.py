```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:])][-1::-1] if i < numbers[-1]]
```
Here is a Python function that solves the problem. It takes two list of integers, generates a new list with the rolling maximum elements, and returns this list.