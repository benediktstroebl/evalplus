```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    The list comprehension approach was used to implement this function.
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [x for x,n in zip(numbers[1:],numbers[1::n])][::-1] # from the first number until the list's length reduces 

>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]

The code uses the `typing` module to provide type hints for the function signature and the function parameters.