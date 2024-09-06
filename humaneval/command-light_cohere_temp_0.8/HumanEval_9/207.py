```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [num for num in numbers if num != 0]  # Remove zero elements
    max_index = numbers.count(max(numbers))
    max_element = numbers[max_index]
    rolling_maxes = [max_element]
    
    for i in range(max_index - 1, -1, -1):
        max_element = max(numbers[i], max_element)
        rolling_maxes.append(max_element)
    
    return rolling_maxes
```
This Python function called "rolling_max" accepts a list of integers as input and outputs a new list of integers, which is a rolling maximum elements list found up to the given moment in the sequence.

The function starts by removing any zero elements from the input list to avoid errors. It then identifies the a index of the maximum element in the list using the "count_max" function. After finding the maximum element, the function initializes a list called "rolling_maxes" to store the maximum element encountered so far. 

Then, using a sliding window approach, it iterates through the list in reverse order (from the last element to the first) and updates the "rolling_maxes" list with the current maximum element. The process continues until it maximum element is no longer found in the sequence, at which point the function returns the "rolling_maxes" list.