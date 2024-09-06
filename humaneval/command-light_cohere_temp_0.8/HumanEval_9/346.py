```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    Args:
        numbers (List[int]): The input list of integers.
    Returns:  a list of integers, the same order, but with the maximum elements of each rolling window until the given moment.
    """
   
    list of integers, the same order, but with the maximum elements of each rolling window until the given moment in the sequence.
    """
```
def test_rolling_max():
    numbers = [1, 2, 3, 2, 3, 4, 2]
    expected = [1, 2, 3, 3, 3, 4, 4]
    got = rolling_max(numbers)
    assert expected == got
```
The test_rolling_max function creates a list of numbers and passes it to the rolling_max function. It then asserts that the expected and got are equal.