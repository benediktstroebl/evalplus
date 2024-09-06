from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    window = []
    max_in_window = -float('inf')
    for x in numbers:
        max_in_window = max(max_in_window, x)
        window.append(max_in_window)
    return window

