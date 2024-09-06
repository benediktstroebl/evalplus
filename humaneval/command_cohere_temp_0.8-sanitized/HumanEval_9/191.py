from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers to compute rolling max for.
        rolling_window (int): Size of the rolling max window.

    Returns:
        List[int]: List of length rolling_window containing the maximum elements encountered so far.
    """
    if not numbers or rolling_window <= 0:
        return []

    result = [float('-inf')] * rolling_window
    result[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(i - rolling_window + 1):
            if numbers[j] > numbers[i]:
                result[j] = numbers[i]

    return result