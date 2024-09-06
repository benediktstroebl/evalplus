from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far, max_ending_here = numbers[0], numbers[0]
    rolling_max_list = []

    for element in numbers:
        max_ending_here = max(max_ending_here, element)
        rolling_max_list.append(max_so_far)
        max_so_far = max(max_so_far, max_ending_here)

    return rolling_max_list

