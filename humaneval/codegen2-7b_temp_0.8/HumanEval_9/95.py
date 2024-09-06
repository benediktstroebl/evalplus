from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    i = 0
    for num in numbers:
        if num < numbers[i]:
            rolling_max.append(num)
        else:
            rolling_max.append(rolling_max[-1])
        i += 1
    return rolling_max

