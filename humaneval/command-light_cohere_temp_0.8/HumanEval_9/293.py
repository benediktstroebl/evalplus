```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list of integers
    > starting with 0 and ending with the last element.
    Args:
        numbers (List[int]): A list of integers.
    Returns: list of rolling maximum elements.
    """

    expected return is list of integers
    """
    return [num for num, num+1 in zip(numbers[:-len(numbers)+1], numbers)]

# test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```