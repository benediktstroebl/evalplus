```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(f" Rolling Maximum: {sorted(rolling_max(numbers))}")
```
This code defines a function `rolling_max` which generates a list of the maximum elements from the previous two elements in the list, starting from the second element. It then returns this list of the maximums, which are the two previous numbers that have the maximum value when considering their cumulative effect.