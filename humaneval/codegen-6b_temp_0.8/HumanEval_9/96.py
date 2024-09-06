from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    maximum = -INF
    current_maximum = -INF

    for i in range(len(numbers)):
        current_maximum = max(current_maximum + numbers[i], numbers[i])
        result.append(current_maximum)

    return result

