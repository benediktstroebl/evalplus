from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
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
        return [float('-inf')] * rolling_window

    rolling_maxes = [float('-inf')] * rolling_window
    rolling_maxes[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(rolling_window - 1):
            if numbers[i] > rolling_maxes[j]:
                rolling_maxes[j + 1:] = rolling_maxes[j:] + [numbers[i]]
                rolling_maxes[j] = numbers[i]

    return rolling_maxes