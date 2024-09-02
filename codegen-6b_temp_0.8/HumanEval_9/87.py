from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    prev = None
    for n in numbers:
        if prev is None:
            result.append(n)
            prev = n
            continue
        if n > prev:
            result.append(n)
        else:
            result.append(prev)
        prev = n
    return result

