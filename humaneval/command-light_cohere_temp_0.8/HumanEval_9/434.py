```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the rolling maximum element found in the given list of integers.
    Every time the saw, we look at a value in the sequence, 
    we keep track of the maximum value we have seen so far.

    When the maximum value and every moment, we 
    start from the first number in the sequence.
    """

    rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [num for num in numbers]  # Convert the input list into a Python list
    return [num for num in sorted(numbers)] + [numbers[-1]]  # Add the last element as the rolling maximum
```
This Python script defines a function called **rolling_max** that takes a list of integers as input and returns a new list that contains the rolling maximum element in the sequence. It does this by first converting the list into a Python list, sorting the list in ascending order, and then adding the last element to the result.

This solution is self-contained and does not require any external functions or modules.