from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_ = numbers[0]
    max_rolling = [max_]

    for i in range(1, len(numbers)):
        max_ = max(numbers[i], max_ + numbers[i])
        max_rolling.append(max_)

    return max_rolling

