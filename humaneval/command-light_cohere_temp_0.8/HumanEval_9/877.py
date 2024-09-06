```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements in a given list of integers.
    numbers = [1, 2, 3, 4, 2, 3, 5]
    return [x for x in numbers if x == max(numbers[::i:], numbers[:i+1]) for i in range(len(numbers))]
    """
    return [x for x in numbers if x == max(numbers[::i:], numbers[:i+1]) for i in range(len(numbers))]

# Tests
numbers = [1, 2, 3, 4, 2, 3, 5]
print(rolling_max(numbers))  # expected output: [1, 2, 3, 3, 3, 4, 4]
```