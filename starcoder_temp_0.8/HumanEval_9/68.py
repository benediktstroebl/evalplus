from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = -math.inf
    max_so_far_idx = 0
    result = []
    for i, number in enumerate(numbers):
        if number > max_so_far:
            max_so_far = number
            max_so_far_idx = i
        result.append(max_so_far)
    return result

