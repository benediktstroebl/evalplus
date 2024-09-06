```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    The list of rolling maximum elements is returned.
    """
    algorithm is inspired from:
    https://www. Pudelings's rolling max sequence formula, which
    uses an array of any data type.
    This implementation is provided in the linked article:
    https://www. report programming.io/p video sequence of
    single source integer
    number, then return the maximum integer in
    the array.
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = [x for x in numbers if x > max([numbers[::i] for i in range(len(numbers))])]
    return result
```