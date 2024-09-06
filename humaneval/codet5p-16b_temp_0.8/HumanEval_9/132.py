from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    rolling_max = max(numbers)
    result.append(rolling_max)
    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            rolling_max = max(rolling_max, numbers[i + 1])
        else:
            rolling_max = numbers[i + 1]
        result.append(rolling_max)
    return result

