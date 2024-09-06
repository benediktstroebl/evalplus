from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 2
    max_window = max(numbers)
    for n in range(window_size, len(numbers)):
        max_num = max(numbers[n-window_size:n])
        if max_num > max_window:
            max_window = max_num
    return [x for x in numbers if x <= max_window]

