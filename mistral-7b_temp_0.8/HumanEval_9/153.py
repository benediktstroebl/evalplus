from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximums = []
    current_maximum = None

    for number in numbers:
        if current_maximum is None or number > current_maximum:
            current_maximum = number
        maximums.append(current_maximum)
    return maximums

