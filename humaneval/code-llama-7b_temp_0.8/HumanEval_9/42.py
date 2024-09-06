from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    rolling_max_so_far: int = numbers[0]
    for num in numbers:
        rolling_max_so_far = max(rolling_max_so_far, num)
        result.append(rolling_max_so_far)
    return result

