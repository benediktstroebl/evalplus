Here is a self-contained Python script that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in a given list of integers.
    Args:
    numbers (List[int]): A list of integers
    Returns:
    List[int]: A list of rolling maximum elements.
    """
   
    specific test cases:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([1, 2, 3, 4, 5])
    [1, 3, 4, 5]
    >>> rolling_max([10, 2, 3, 4, 5])
    [10, 3, 4, 5]
    """
    if not numbers:
        return []

    # Initialize the list with the first element, which is also the maximum
    rolling_max_list = [numbers[0]]

    # Append the current maximum element to the list
    rolling_max_list.append(numbers[i])
    i = 1

    # Update the current maximum element with the next element in the list
    numbers[i] = numbers[i - 1] + 1

    # Append the next element in the list to the list
    rolling_max_list.append(numbers[i])
    i += 1

    return rolling_max_list
```
This Python code defines a function called "rolling_max" that calculates and returns a list of rolling maximum elements from a given list of integers. The function uses the specific test cases to demonstrate its functionality.