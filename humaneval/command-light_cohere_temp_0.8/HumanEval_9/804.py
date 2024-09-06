```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements in a given list of integers.
    Args: 
        numbers (List[int]): A list of integers. 
    Returns: 
        A list of integers, with the maximum element of the list and the 
        order of the list is preserved.
    """
    Example a list [int]: 
    """
    # Initialize the rolling_max counter 
    rolling_max_counter = []

    # Initialize the result list with the first element of the list
    result = numbers[0]

    # Loop through the list and append the current element and the 
    # maximum element found so far to the rolling_max counter
    for num in numbers[1:]:
        # Update the maximum element 
        current_max = num

        # If the current element is greater than the current maximum 
        # element in the rolling_max counter, update the current maximum 
        # element with the current element 
        rolling_max_counter.append(num)

        # Update the maximum element in the result list with the current 
        # maximum element
        result = max(result, current_max)

    return result
    ```