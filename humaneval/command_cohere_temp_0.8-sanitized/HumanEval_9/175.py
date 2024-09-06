from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """
    Generate a list of rolling maximum elements found in the list within a rolling window.
    
    Args:
    - numbers (list): Input list of integers.
    - rolling_window (int): Window size to compute the rolling maximum.
    
    Returns:
    - list: Sequence of rolling maximum elements.
    """
    
    # Initiate the rolling maximum and minimum variables
    rolling_max_curr = numbers[0]
    rolling_max_prev = numbers[0]
    
    result = [rolling_max_curr]
    
    # Iterate through the list to update the rolling maximum
    for i in range(1, len(numbers)):
        rolling_max_curr = max(numbers[i], rolling_max_prev)
        rolling_max_prev = rolling_max_curr
        
        result.append(rolling_max_curr)
    
    return result
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3
result = rolling_max(numbers, rolling_window)