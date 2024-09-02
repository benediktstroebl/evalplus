from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_el: Tuple[int, int] = (0, 0)
    result: List[int] = []
    for i, number in enumerate(numbers):
        max_el = max_el if max_el[0] > number else (i, number)
        result.append(max_el[1])
    return result

