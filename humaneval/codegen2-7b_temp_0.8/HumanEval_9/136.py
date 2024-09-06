from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max = -1

    for num in numbers:
        if num > previous_max:
            previous_max = num
        else:
            previous_max = max(previous_max, num)

    return previous_max

