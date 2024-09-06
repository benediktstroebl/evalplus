from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """Return the rolling maximum over a rolling window of size rolling_window

    Args:
        numbers (List[int]): list of integers to be processed
        rolling_window (int):  size of the rolling window

    Returns:
        List[int]: list of size len(numbers) with the rolling maximums
    """
    # Initialization
    result, max_so_far = [-1] * len(numbers), numbers[0]

    # Compute rolling max
    for i in range(rolling_window - 1, len(numbers)):
        current = numbers[i]
        if current > max_so_far:
            max_so_far = current
        result[i] = max_so_far

    return result