from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_values = [numbers[0]]
    for idx in range(1, len(numbers)):
        max_values.append(max(numbers[idx], max_values[-1]))

    return max_values

