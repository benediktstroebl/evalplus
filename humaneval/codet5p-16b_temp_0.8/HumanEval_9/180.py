from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maxes = []
    for i in range(len(numbers)):
        num = numbers[i]
        rolling_maxes.append(num)
        for j in range(i + 1, len(numbers)):
            if numbers[j] > num:
                num = numbers[j]
        rolling_maxes.append(num)
    return rolling_maxes

