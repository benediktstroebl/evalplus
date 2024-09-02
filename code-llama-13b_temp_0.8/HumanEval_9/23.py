from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max: int = float("-inf")
    res: List[int] = []
    for n in numbers:
        if n > previous_max:
            previous_max = n
        res.append(previous_max)
    return res

