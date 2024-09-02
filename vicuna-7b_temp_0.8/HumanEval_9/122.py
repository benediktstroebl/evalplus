from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Get the index of the latest maximum value
    max_index = len(numbers) - 1
    
    # Initialize a variable to store the rolling maximum value
    rolling_max_value = numbers[max_index]
    
    # Initialize a variable to store the index of the current maximum value
    rolling_max_index = max_index
    
    # Initialize a variable to store the list of rolling maximum value
    rolling_max_list = []
    
    # Increment the rolling maximum index to the next value
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max_value:
            rolling_max_value = numbers[i]
            rolling_max_index = i
    
    # Update the rolling maximum list with the new value and index
    rolling_max_list.append((rolling_max_value, rolling_max_index))
    
    # Return the updated rolling maximum list
    return rolling_max_list

