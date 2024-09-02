from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    l, r = 0, 1
    res = [numbers[0]]
    while r < len(numbers):
        if numbers[r] > numbers[l]:
            res.append(numbers[r])
        else:
            res.append(numbers[l])
        l += 1
        r += 1
    return res

