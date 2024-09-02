from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = []
    max_i = 0
    for i in range(len(numbers)):
        if i == 0:
            rolling_max.append(numbers[i])
            max_i = i
        elif numbers[i] > numbers[i - 1] and i!= max_i:
            rolling_max.append(numbers[i])
            max_i = i
        else:
            rolling_max.append(numbers[i])
    return rolling_max

