from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    rolling_max_el = float('-inf')
    for idx, number in enumerate(numbers):
        rolling_max_el = max(number, rolling_max_el)
        result.append(rolling_max_el)
    return result

