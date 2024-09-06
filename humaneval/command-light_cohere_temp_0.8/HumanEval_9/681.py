```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements from the input list.

    Numbers must be positive in ascending order.
    Numbers should be non-negative integers.

    Returns the core list of integers, ordered in ascending.
    """
    must be numbers, not strings, floats, etc
    """

    # convert list of integers to set for set operations
    numbers = set(numbers)

    # take first element of the sorted list
    max_element = next(numbers)[1]

    # initialize a list to store rolling max elements
    rolling_max_elements = [max_element]

    # get the rest of the elements in sorted order
    for num in numbers:
        # find the maximum element that is less than or equal to the current element
        max_element = max( (max_element, num) )
        # add the rolling max element to the list
        rolling_max_elements.append(max_element)

    return rolling_max_elements

# Test case:
numbers = [1, 2, 3, 4, 5]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # expected output: [1, 2, 3, 3, 4, 5]
```
This script defines a function called `rolling_max` that takes a list of integers and returns a new list of the rolling maximum elements. The function converts the time the list of integers to a set for efficient set operations, and then it sorts the numbers in ascending order. Next, the first element is taken from the sorted list and stored in the `max_element` variable. The `rolling_max_elements` list is initialized with the `max_element`. Then, using the `max()` function with the current element and the `max_element` variable, the maximum element that is less than or equal to the current element is found and stored in the `max_element` variable. The `rolling_max_elements` list is then updated with the new rolling maximum element. Finally, the function returns the list of integers.