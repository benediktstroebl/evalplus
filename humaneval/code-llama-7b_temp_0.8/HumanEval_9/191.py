from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_numbers: List[int] = []
    for i in range(0, len(numbers)):
        if i == 0:
            rolling_max_numbers.append(numbers[0])
            continue
        rolling_max_numbers.append(max(rolling_max_numbers[i-1], numbers[i]))
    return rolling_max_numbers

