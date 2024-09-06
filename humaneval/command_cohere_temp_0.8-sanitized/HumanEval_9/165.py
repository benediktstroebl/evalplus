from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers.
        rolling_window (int): The rolling window size.

    Returns:
        List[int]: The list of rolling maximum elements.
    """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_indices = [i for i, num in enumerate(numbers) if num == max(numbers[:i + rolling_window])]
    
    return [numbers[max_idx] for max_idx in max_indices]