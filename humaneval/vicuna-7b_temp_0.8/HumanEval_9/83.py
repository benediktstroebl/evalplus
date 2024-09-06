from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    from itertools import zip_longest
    from collections import deque

    window_size = 3  # you can change this to change the window size
    window = deque(numbers[:-window_size])
    rolling_max_list = []

    for i in range(1, len(numbers) + 1):
        current_max = max(window)
        window.pop(0)
        rolling_max_list.append(current_max)

        if i == len(numbers):
            window = deque(numbers)
        else:
            window.append(numbers[i])

    return rolling_max_list

