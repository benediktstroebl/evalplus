from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_elem_so_far = max(numbers)
    result: List[int] = []
    for i in numbers:
        max_elem_so_far = max(max_elem_so_far, i)
        result.append(max_elem_so_far)
    return result

