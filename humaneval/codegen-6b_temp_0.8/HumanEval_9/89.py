from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximum, result = numbers[0], []
    for i in numbers:
        if i > maximum:
            maximum, result = i, [maximum]
        elif i == maximum:
            maximum, result = max(maximum, i), list(result) + [maximum]
        else:
            result = []
    return result

