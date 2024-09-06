from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    res = []
    max_so_far = 0
    for x in numbers:
        if x > max_so_far:
            max_so_far = x
        res.append(max_so_far)
    return res

