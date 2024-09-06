```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generate a list of rolling maximum elements in a given list of integers.
    Each element in the max sequence is the maximum of its current index and 
    previous elements. 
    >>> e.g. [1, maximum, elements: [2,3,2,3,2,3], 
    [1,2,3,3,3,3,4,4]
    """
    # mapping to store the previous maximum element and current index 
    max_map = {}

    # initializing the first element in the map 
    current_index = 0

    for element in numbers:
        # checking if the current element is not in the map
        if element in max_map:
            max_map[element] = element
        else:
            max_map[element] = element  # otherwise set the element to its current value
        # calculating the current maximum element
        current_max = max(max_map.get(current_index, max_map.get(current_index - maximum element found)
        max_map[element] = current_max
        current_index += 1

    return max_map[numbers[current_index]]
``` 
This Python function rolling_max takes a list of integers numbers as input and returns a list of integers. It uses a mapping to store the previous maximum element and current index, iterating over the list of integers.