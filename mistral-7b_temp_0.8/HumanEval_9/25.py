from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # your code here
    res = []
    for idx, item in enumerate(numbers):
        if idx == 0:
            res.append(item)
        else:
            if item >= res[-1]:
                res.append(item)
            else:
                res[-1] = item
    return res

