from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = [numbers[0]]
    for current_idx in range(1, len(numbers)):
        current = numbers[current_idx]
        previous = numbers[current_idx - 1]
        if previous > current:
            result.append(previous)
        else:
            result.append(current)
    return result

