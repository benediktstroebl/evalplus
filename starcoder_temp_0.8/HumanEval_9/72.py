from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    if not numbers:
        return numbers

    result = []

    for num in numbers:
        if not result or num > result[-1]:
            result.append(num)
        else:
            result.append(result[-1])

    return result

