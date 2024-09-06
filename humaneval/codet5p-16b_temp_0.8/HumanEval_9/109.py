from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    res: List[int] = []
    maximum: int = None
    for n in numbers:
        if maximum is None or n > maximum:
            maximum = n
        res.append(maximum)
    return res

