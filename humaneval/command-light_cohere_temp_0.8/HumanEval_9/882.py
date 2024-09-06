```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    :return [ [i for i, num in enumerate(numbers)] if num >= rolling_max[i] == False][::-1]
    return rolling_max[::-1]

numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # Output: [4, 3, 3, 3, 2, 2, 1]
```