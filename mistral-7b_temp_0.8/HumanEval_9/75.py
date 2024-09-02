from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_max: int = 0
    ret: List[int] = []
    for num in numbers:
        if last_max < num:
            last_max = num
            ret.append(last_max)
        else:
            ret.append(last_max)
    return ret

