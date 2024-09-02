from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(max(numbers[i], result[i - 1]))
    return result

