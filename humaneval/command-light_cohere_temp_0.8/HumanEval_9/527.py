```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in sorted((n, x) for n, x in zip(numbers[1:], numbers))]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [1, 2, 3, 2, 3, 4, 2, 5]
result = rolling_max(numbers)
print(result)

numbers = [1, 2, 3, 1, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
The code defines a function `rolling_max` that takes a list of integers as input and generates a new list that contains the maximum element from the list after each moment. It uses the  a technique to cycle through the sorted list and stores the maximum element found on each cycle. The output will be a list of integers that represent the maximum element found in each corresponding moment.