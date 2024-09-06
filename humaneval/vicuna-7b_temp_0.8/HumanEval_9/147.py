from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 1
    current_max = numbers[0]

    for i in range(1, len(numbers)):
        window_size -= 1
        if window_size == 0:
            current_max = numbers[i]
            break

    return [current_max] + [numbers[j] for j in range(1, len(numbers)) if j % window_size == 0]

