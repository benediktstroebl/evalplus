from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """
    Generate a list of rolling maximum elements found in the given list of integers.

    Args:
        numbers (List[int]): Input list of integers.
        rolling_max_window (int): Window size for computing the rolling maximum.

    Returns:
        List[int]: List of rolling maximum elements.
    """
    if not numbers:
        return []

    rolling_max_result = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - rolling_max_window]:
            rolling_max_result.append(numbers[i])
        else:
            rolling_max_result.append(rolling_max_result[i - rolling_max_window])

    return rolling_max_result
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_window = 3