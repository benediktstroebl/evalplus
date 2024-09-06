```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns a list of rolling maximum elements found until a given moment 
    in the sequence.
    Args: numbers(List[int]): a list of integers
    Returns: List[int]: a list of rolling maximum elements
    """
    return [num for num in numbers for _ in range(len(numbers))] if numbers else [].images[0]

# Unit tests
def test_rolling_max():
    assert rolling_max([1, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
```