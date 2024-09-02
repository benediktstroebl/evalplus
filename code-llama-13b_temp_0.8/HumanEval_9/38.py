from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_el = numbers[0]
    rolling_max_el_index = 0
    result = []
    for i, el in enumerate(numbers):
        if el >= rolling_max_el:
            rolling_max_el = el
            rolling_max_el_index = i
        result.append(rolling_max_el)
    return result

