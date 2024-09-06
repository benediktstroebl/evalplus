```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until the given moment.
    >>> [1, 2, 3, 2, 3, 4, 2] 
    [1, 2, 3, 3, 3, 4] 
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [x for x in numbers if x != numbers[-1] and x >= numbers[-1]]

# Test cases
numbers_test = [1, 2, 3, 4, 3, 5]

result_test = rolling_max(numbers_test)
print(result_test)

```