from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    result = [max_so_far]
    for current in numbers[1:]:
        max_so_far = max(current, max_so_far)
        result.append(max_so_far)
    return result

