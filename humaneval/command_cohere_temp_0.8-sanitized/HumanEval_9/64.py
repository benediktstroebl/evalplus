from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    
    Args:
    - numbers (List[int]): The list of integers to process.
    - rolling_window (int): The size of the rolling maximum window.
    
    Returns:
    - List[int]: A new list containing the rolling maximum elements.
    """
    
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return numbers[:]

    rolling_max_vals = [numbers[0]]
    for i in range(1, len(numbers)):
        max_val = max(rolling_max_vals[-rolling_window:][1:])
        rolling_max_vals.append(max_val)

    return rolling_max_vals