Here's a self-contained Python function that generates a list of rolling max elements from a given list of integers:
```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the maximum element in the list and then repeatedly subtract it from the list to get the rolling maximum elements.
    Return a list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    """
    list of integers.
    > rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize a list to store the rolling maximum elements
    result = [num for num in numbers]
    while len(result) < len(numbers):
        # Get the current maximum element and add it to the result list
        current_max = max(result)
        result.append(current_max -
        # Remove the current maximum element and all smaller elements from the list
        numbers = list(filter(lambda x: x < current_max, numbers)))
    return result
```
This function takes a list of integers as input and returns a list of integers that are the rolling maximum elements found in the given list.