from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    rolling_maximums = []

    for number in numbers:
        rolling_maximums.append(max(number, max_so_far))
        max_so_far = max(max_so_far, number)

    return rolling_maximums

