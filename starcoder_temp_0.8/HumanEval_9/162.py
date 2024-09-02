from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    current_max: int = numbers[0]
    rolling_max: List[int] = [current_max]

    for i in range(1, len(numbers)):
        current_number = numbers[i]
        current_max = max(current_number, current_max)
        rolling_max.append(current_max)

    return rolling_max

