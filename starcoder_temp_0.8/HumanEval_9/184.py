from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maximum = []

    for index, _ in enumerate(numbers):
        try:
            rolling_maximum.append(max(numbers[index:index + 3]))
        except ValueError:
            # list is too short
            rolling_maximum.append(numbers[index])

    return rolling_maximum
