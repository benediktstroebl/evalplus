from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within the rolling_length window.
    
    :param numbers: List of integers to analyze.
    :param rolling_length: Length of the rolling window.
    :return: List of size len(numbers) where each element is the maximum within the rolling_length window.
    """
    if rolling_length <= 0:
        raise ValueError("Rolling length must be a positive integer")
    
    if len(numbers) < rolling_length:
        return [0] * len(numbers)  # Return a list of zeros if not enough elements
    
    res = [0] * len(numbers)
    win_start = 0
    win_end = rolling_length - 1
    
    for idx, num in enumerate(numbers):
        # Update window if we hit the right boundary
        if idx == win_end:
            win_start = win_end + 1
            win_end = min(win_start + rolling_length - 1, len(numbers) - 1)
        
        # Update maximum if necessary
        if num > res[win_start]:
            res[win_start] = num
        
        if num > res[win_end]:
            res[win_end] = num
    
    return res