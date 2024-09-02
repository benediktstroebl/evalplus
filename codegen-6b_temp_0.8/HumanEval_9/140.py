from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    for i, e in enumerate(numbers[1:], start=1):
        if e > result[i - 1]:
            result.append(e)
        else:
            result.append(result[i - 1])
    return result

