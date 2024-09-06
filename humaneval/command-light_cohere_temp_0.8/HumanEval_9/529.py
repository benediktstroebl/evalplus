```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in a given list.

    Parameters: List[int]: List of integers
    Returns: List[int], list of rolling maximum elements found until a given moment in the sequence.
    """
    takes a list of numbers as input and uses the list comprehension to generate a new list that contains the maximum element found in the list after each iteration. The list comprehension uses the maximum element from the list and assigns it to a new list until it finds the element that corresponds to the end of the list.

Tests:
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
>>> rolling_max([4, 4, 4, 4])
[4, 4, 4]
``` 
This Python script defines a function called `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements found in the list. The `rolling_max` function uses the list comprehension and the `max` function to find the maximum element in the list after each iteration.