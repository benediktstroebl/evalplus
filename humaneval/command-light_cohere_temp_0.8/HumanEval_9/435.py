```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4, 4, 4, 5])
    [4, 4, 4]
    >>> rolling_max([10, 20, 30])
    []
    """
    rolling_maxes = []
    while True:
        current_max = max(numbers[:])
        rolling_maxes.append(current_max)
        numbers.append(numbers[-1])
        break if numbers[-1] == current_max
rolling_maxes: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function called rolling_max, which takes a list of integers as input and returns a new list of the maximum elements found in that list, but only the first occurrence of that element will be present in the output. The script then demonstrates the result of the function with a couple of test cases.