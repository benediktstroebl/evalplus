from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elem = []
    max_curr = None
    for num in numbers:
        if max_curr is None:
            max_curr = num
        else:
            if num > max_curr:
                max_curr = num
        max_elem.append(max_curr)
    return max_elem

