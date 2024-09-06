```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment
    in the sequence.
    Parameters:
        numbers (List[int]): A list of integers
    Returns:
        List[int]: A list of rolling maximum elements found until the given moment.
    """

Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize a list to store the rolling maximum elements
    rolling_max_elements = []

    # Iterate through the numbers list and append the maximum element encountered so far to the list
    for num in numbers:
        rolling_max_elements.append(num if num > rolling_max_elements[-1]) 
        else rolling_max_elements.append(rolling_max_elements[-1])

    return rolling_max_elements
```
The code defines a function `rolling_max` that takes a list of integers as an argument and returns a list of rolling maximum elements found in the input list. 

The function uses a list to store the rolling maximum elements and iterates through the numbers list. 

For each number, it checks if the current number is greater than the last element in the list, and if so, it appends the current number to the list. If the current number is not greater, it keeps the last element in the list.