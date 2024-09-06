from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 2:
        raise ValueError(f"{numbers} needs to contain at least two elements")

    max_so_far = 0
    rolling_max = []
    for num in numbers:
        max_so_far = max(num, max_so_far)
        rolling_max.append(max_so_far)
    return rolling_max

