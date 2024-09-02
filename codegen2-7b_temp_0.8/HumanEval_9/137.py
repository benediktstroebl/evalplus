from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    res = []
    window = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] < window:
            res.append(window)
            window = max(numbers[i + 1:])
        else:
            window = numbers[i]
    return
