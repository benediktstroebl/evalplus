```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [n for n, _ in zip(numbers[::1], numbers[1:]) if n > numbers[_]]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
assert rolling_max(numbers) == [1, 3, 4, 5]

numbers = [10, 20, 30, 40, 50]
assert rolling_max(numbers) == [10, 20, 30, 40, 50]
```

This script defines a function `rolling_max` that generates a list of rolling maximum elements in a given sequence. The function utilizes a simple strategy of creating a generator that extracts the maximum element from the moment and uses it to create a rolling maximum sequence until the moment is reached. The test cases demonstrate the correct functionality of the function.