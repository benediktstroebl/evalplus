from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    cache = numbers[0]
    maximum = [cache]
    for number in numbers[1:]:
        cache = max(cache, number)
        maximum.append(cache)
    return maximum

