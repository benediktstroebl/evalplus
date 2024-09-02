from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_result: List[int] = []
    rolling_max_result.append(numbers[0])
    for i, value in enumerate(numbers):
        if i == 0:
            continue
        if numbers[i] >= numbers[i - 1]:
            rolling_max_result.append(numbers[i])
        else:
            rolling_max_result.append(rolling_max_result[-1])

    return rolling_max_result

