from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The size of the rolling window to look at to find the rolling maximum.
    
    Returns:
        List[int]: A list of integers, where each integer represents the maximum of rolling_window size interval found
                    in the original sequence.
    """
    
    if not numbers or not rolling_window:
        return []

    # Sort the input list to find the maximum elements easily.
    sorted_numbers = sorted(numbers)
    
    # Calculate the rolling maximum elements for each index in the rolling window.
    rolling_max_elements = [sorted_numbers[i] for i in range(len(sorted_numbers)-rolling_window+1)]
    
    return rolling_max_elements