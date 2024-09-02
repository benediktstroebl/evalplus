from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    ret = [None] * len(numbers)
    ret[0] = numbers[0]
    for i in range(1, len(numbers)):
        if ret[i - 1] > numbers[i]:
            ret[i] = ret[i - 1]
        else:
            ret[i] = numbers[i]
    return ret

