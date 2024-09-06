from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    res = []
    for i in range(len(numbers)):
        curr_max = max(res + [numbers[i]]) if i else numbers[i]
        res.append(curr_max)
    return res

