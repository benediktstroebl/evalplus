from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maximum = []
    maximum = None

    for index, number in enumerate(numbers):
        if maximum is None:
            maximum = number
        elif number > maximum:
            maximum = number
        rolling_maximum.append(maximum)

    return rolling_maximum

