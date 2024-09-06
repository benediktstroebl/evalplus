from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_value = 0
    for i in numbers:
        if i > max_value:
            max_value = i
        elif i == max_value:
            max_value += 1
        else:
            result.append(max_value)
            max_value = i
    result.append(max_value)
    return
