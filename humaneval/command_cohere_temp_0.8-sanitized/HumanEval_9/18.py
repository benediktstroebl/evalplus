from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers.
        window_size (int): Window size of the rolling maximum.

    Returns:
        List[int]: Rolling maximum elements within the window.
    """

    if not numbers:
        return []

    if window_size <= 0 or window_size > len(numbers):
        raise ValueError("Invalid window size. Please provide a positive integer")

    max_list = [numbers[0]]

    for i in range(1, len(numbers)):
        max_list.append(max(numbers[i], max_list[i - window_size]))

    return max_list
numbers = [1, 2, 3, 2, 3, 4, 2]