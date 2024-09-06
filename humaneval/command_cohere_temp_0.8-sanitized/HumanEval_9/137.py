from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the current moment
    in the sequence. Outputs will be overwritten if they coincide.

    Parameters:
        numbers (List[int]): List of integers to be inspected.
        rolling_window (int): Window size to look at to find the rolling maximum for.

    Returns:
        List[int]: Rolling maximums up to the current moment.
    """

    if not numbers or not rolling_window:
        return []

    rolling_maxes = [numbers[0]]

    for i in range(1, len(numbers)):
        if i - rolling_window >= 0:
            rolling_maxes.append(max(numbers[i-rolling_window:i+1]))
        else:
            rolling_maxes.append(max(numbers[i:i+rolling_window]))

    return rolling_maxes
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3