```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of the rolling maximum elements found in the given list.
    numbers = [2, 3, -1, 4, -3, 9, 10]
    return [max(numbers[i:i+2]) for i in range(len(numbers)-1)]

numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)

```