from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maxes = [None] * len(numbers)
    max_length = 0
    maximum = 0
    for idx, number in enumerate(numbers):
        if number > maximum:
            maximum = number
            max_length = 1
        elif number == maximum:
            max_length += 1
        else:
            if max_length > 1:
                max_length -= 1
            else:
                rolling_maxes[idx] = maximum
    for idx in range(len(numbers)):
        if idx >= max_length:
            rolling_maxes[idx] = None
        else:
            rolling_maxes[idx] = maximum
    return rolling_maxes

