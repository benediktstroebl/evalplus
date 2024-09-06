from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maximums = []
    rolling_maximum = numbers[0]

    for number in numbers:
        if rolling_maximum < number:
            rolling_maximum = number
        rolling_maximums.append(rolling_maximum)

    return rolling_maximums

