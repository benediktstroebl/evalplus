from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    if len(numbers) < 1:
        return []

    rolling_max = [numbers[0]]
    for number in numbers[1:]:
        rolling_max.append(max(number, rolling_max[-1]))
    return rolling_max

