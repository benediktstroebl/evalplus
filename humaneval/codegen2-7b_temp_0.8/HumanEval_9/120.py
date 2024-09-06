from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximum: List[int] = []
    for number in numbers:
        if not maximum or number > maximum[-1]:
            maximum.append(number)
        else:
            maximum[-1] = number

    return maximum

