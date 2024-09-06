```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the rolling maximum element in a list.
    Returns a
    list of rolling maximum elements found up until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [num for num in numbers if num != 0]  # Remove zeros
    numbers.append(numbers[-1])  # Add the last element to the list
    max_element = numbers[0]
    current_element = numbers[1]
    current_moment = 1
    rolling_maxs = [max_element]  # Initialize the list of rolling max elements
    while current_element > 0:
        if current_element > max_element:
            max_element = current_element
        rolling_maxs.append(current_element)
        current_element = current_element - 1
        current_moment += 1
    return rolling_maxs
```
This function accepts a list of integers as an argument and uses a sliding window approach to determine the rolling maximum element in that list. It ensures that the approach eliminates the element from the list, adds the last element to the rolling maximums, and then repeatedly loops through the list, updating the rolling maximums with each element that exceeds the current maximum. 

The function is simple and efficient, with a time complexity of O(n), where n is the length of the input list.