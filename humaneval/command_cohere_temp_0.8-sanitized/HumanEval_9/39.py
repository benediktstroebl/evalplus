from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    
    Args:
        numbers (List[int]): List of integers.
        window_size (int): Window size ( exorbitantly large to handle all max values).
    
    Returns:
        List[int]: Rolling maximum elements in the list.
    """
    if not numbers:
        return []
    if len(numbers) < window_size:
        return [max(numbers)]
    rolling_maxes = [max(window) for window in zip_longest(*[iter(numbers)]*window_size)]
    return rolling_maxes