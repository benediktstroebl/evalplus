from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    r = [numbers[0]]
    for i in numbers[1:]:
        if i > r[-1]:
            r.append(i)
        else:
            r.append(r[-1])
    return r

