from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_ = []
    for i in range(len(numbers)):
        if max_ and numbers[i] >= max_[-1]:
            max_.append(numbers[i])
        else:
            max_.append(numbers[i])
    return max_

