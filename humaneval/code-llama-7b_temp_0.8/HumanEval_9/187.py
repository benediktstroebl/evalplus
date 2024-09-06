from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maximum: List[int] = []
    rolling_maximum.append(numbers[0])
    for index in range(1, len(numbers)):
        current = numbers[index]
        rolling_maximum.append(max(rolling_maximum[index - 1], current))
    return rolling_maximum

