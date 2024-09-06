```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Return a list of the rolling maximum elements in a given list of integers.
    Each element in the maximum rolling sequence will be returned.
    """

    list comprehension, along with a loop is used to implement this function.
    """
    list comprehension and a loop are used to generate a list of rolling maximum elements in a given list of integers.

test_rolling_max():
    """
    Test the rolling_max function with different inputs.
   """
    list1 = [1, 2, 3, 2, 3, 4, 2, 3, 4, 2];
    result = rolling_max(list1)
    assert result == [1, 2, 3, 3, 3, 4, 4]
    """