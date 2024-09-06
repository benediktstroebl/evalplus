from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The rolling window size to look backwards and determine the max for.

    Returns:
        List[int]: A list of the maximum elements seen at each step of the specified rolling window.
    """
    
    if not numbers:
        return []

    return [max(numbers[-window:]) for window in range(rolling_window, len(numbers) + 1)]