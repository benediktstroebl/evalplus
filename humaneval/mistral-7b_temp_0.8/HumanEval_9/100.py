from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 1:
        return []

    result = []

    rolling_maximum = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > rolling_maximum:
            result.append(numbers[i])
            rolling_maximum = numbers[i]
        else:
            result.append(rolling_maximum)

    return result

