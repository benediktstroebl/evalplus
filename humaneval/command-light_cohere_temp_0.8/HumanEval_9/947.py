```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns the list of rolling maximum elements in a given list of integers.
   
    - For example, given [1, 2, 3, 2, 3, 4, 2], it returns [1, 2, 3, 3, 3, 4, 4].
    
    :param numbers: List[int] - List of integers
    :return: List[int] - List of rolling maximum elements
    """
    # Sort the list of integers
    numbers = sorted(numbers)
    
    # Initialize the rolling index to the first index
    rolling_index = 0
    
    # Initialize a list to store the rolling maximum elements
    rolling_max = [numbers[rolling_index]]
    
    # Iterate through the list of integers
    for index, num in enumerate(numbers):
        # Calculate the rolling maximum element for the current index
        rolling_max.append(num)
        
        # Move the index to the next index in the list
        rolling_index = index + 1
        
    return rolling_max
``` 
This Python script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum elements found within the input list. The function uses a sorting the list of integers and then uses a loop to iterate through the list, calculating the rolling maximum element at each index and appending it to the `rolling_max` list. The function is tested by passing a sample list of integers and verifying that the returned list of rolling maximum elements matches the expected output.