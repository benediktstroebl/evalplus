from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_found_so_far = None
    for number in numbers:
        if max_found_so_far is None or max_found_so_far < number:
            max_found_so_far = number
        result.append(max_found_so_far)
    return result

