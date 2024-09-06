```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), range(len(numbers))) if numbers[idx] > numbers[idx - 1]]
```
This code defines a function `rolling_max` that calculates the rolling maximum element in a given list. 

It uses a sorted version of the input list and then compares each element with the previous one, effectively tracking the maximum element as it rolls through the sequence. 

The function returns the list of rolling maximum elements.