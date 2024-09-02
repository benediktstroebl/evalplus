from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    max_ending_here = numbers[0]
    result: List[int] = []
    for n in numbers[1:]:
        max_ending_here = max(n, max_ending_here + n)
        result.append(max_so_far)
        max_so_far = max(max_so_far, max_ending_here)
    result.append(max_so_far)
    return result
