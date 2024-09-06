from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The input list of integers.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list where each element is the maximum of the corresponding window in the input list.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers or not rolling_window:
        return []

    return [max(window) for window in zip_longest(numbers, numbers[1:], fillvalue=float('-inf'))]