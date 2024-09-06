from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers to compute rolling max for.
        rolling_window (int): Size of the rolling max window.

    Returns:
        List[int]: List of length len(numbers) - rolling_window + 1, containing the rolling max elements.
    """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('-inf')] * rolling_window

    res = [float('-inf')] * rolling_window
    res[0] = numbers[0]
    for i in range(1, len(numbers)-rolling_window+1):
        for j in range(i, i+rolling_window):
            if res[j%rolling_window] < numbers[j]:
                res[j%rolling_window] = numbers[j]
    return res