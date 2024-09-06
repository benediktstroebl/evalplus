from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    running_maximums = numbers
    for index in range(len(numbers) - 1):
        running_maximums[index + 1] = max(running_maximums[index + 1], running_maximums[index])

    return running_maximums

