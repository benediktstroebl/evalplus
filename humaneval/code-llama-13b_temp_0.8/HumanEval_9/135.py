from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_num = numbers[0]
    max_rolling = []

    for num in numbers:
        max_num = max(max_num, num)
        max_rolling.append(max_num)

    return max_rolling

