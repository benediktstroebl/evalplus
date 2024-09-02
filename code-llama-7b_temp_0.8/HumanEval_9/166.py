from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far: List[int] = []
    max_elem: int = numbers[0]
    for i in numbers:
        max_elem = max(max_elem, i)
        max_so_far.append(max_elem)
    return max_so_far

