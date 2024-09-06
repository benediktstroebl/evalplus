```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment
    in the sequence.
    Return a list of maximum elements of the form [max(n), n] for each n in numbers.
    """
    list of rolling maximums = []
    for n in numbers:
        rolling_max.append(max(numbers[:n] + [numbers[-1]])[::-1])
    return rolling_max

# Example
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # Output: [2, 3, 3, 3, 3, 4, 4]
```