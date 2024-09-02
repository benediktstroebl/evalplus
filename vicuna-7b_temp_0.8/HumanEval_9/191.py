from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    for i in range(len(numbers)):
        # Select max element from the window of previous elements
        window_start = i
        window_end = i + 1
        if window_end == len(numbers):
            window_end = len(numbers) - 1
        max_element = max(numbers[window_start:window_end])
        # Add the selected max element to the rolling maximum list
        rolling_max.append(max_element)
        # Reset the window of previous elements
        window_start = len(rolling_max) + 1
    return rolling_max

