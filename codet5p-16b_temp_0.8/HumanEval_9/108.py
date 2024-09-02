from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = [numbers[0]]  # init with the first element
    for index in range(1, len(numbers)):
        if numbers[index] >= rolling_max[-1]:
            rolling_max.append(numbers[index])
        else:
            rolling_max.append(rolling_max[-1])

    return rolling_max

