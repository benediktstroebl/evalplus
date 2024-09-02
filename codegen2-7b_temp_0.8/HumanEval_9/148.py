from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_elem = -1
    max_elem = -1
    for elem in numbers:
        if elem == last_elem:
            continue
        last_elem = elem
        if elem > max_elem:
            max_elem = elem
    return [last_elem] + [max_elem] * (len(numbers) - 1
