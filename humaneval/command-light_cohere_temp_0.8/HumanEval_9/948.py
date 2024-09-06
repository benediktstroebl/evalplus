```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Return a list of rolling maximum elements from the given list of integers 
    identified by their index.
    """ 
    - Initialize the a list to store the rolling maximum elements 
    - Initialize the rolling maximum element as the first element of the list
    - Iterate through the list and compare the current element with the rolling maximum element 
    - If the current element is greater, update the rolling maximum element and the index 
    - Repeat until the end of the list
    - Return the list of rolling maximum elements
    """
    # Initialize the list of rolling maximum elements
    result = [num for num in numbers]
    
    # Initialize the index of the rolling maximum element
    i = 0
    
    # Iterate through the list and update the rolling maximum element and its index 
    while i < len(numbers):
        if numbers[i] > result[i]:
            result[i] = numbers[i]
            i += 1
        elif numbers[i] < result[i]:
            break  # To avoid infinite loop in case of sorted list
    return result
``` 
This script defines a rolling_max function that takes a list of integers as input and returns a list of rolling maximum elements identified by their index. The rolling_max function uses a sliding window approach to calculate the rolling maximum element. The output list is then filled with the first number in the input list, and the loop iterates through the list until the current element is smaller than the current rolling maximum element, at which point the loop breaks.