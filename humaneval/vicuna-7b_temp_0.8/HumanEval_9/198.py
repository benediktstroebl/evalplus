from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 5  # maximum length of window to consider
    result = [None] * n
    window_sum = 0
    for i in range(len(numbers) - n + 1):
        window = [numbers[i], numbers[i + 1], numbers[i + 2]]
        window_sum = max(window_sum, max(window))
        if window_sum > result[-1] or result[-1] is None:
            result[window_sum - 1] = window_sum
    return result