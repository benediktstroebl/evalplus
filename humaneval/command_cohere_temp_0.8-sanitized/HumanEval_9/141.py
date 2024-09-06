from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers to compute rolling maximum for.
        rolling_window (int): Window size to compute the rolling maximum for.

    Returns:
        List[int]: List of maximum elements seen until the current window in the sequence.
    """
    
    if not numbers or not rolling_window:
        return []

    rolling_maxes = [numbers[0]]

    for i in range(1, len(numbers)):
        max_element = numbers[i]
        for j in range(i - rolling_window + 1, i):
            if numbers[j] > max_element:
                max_element = numbers[j]

        rolling_maxes.append(max_element)

    return rolling_maxes
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3