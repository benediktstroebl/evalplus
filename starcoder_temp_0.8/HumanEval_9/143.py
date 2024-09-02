from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_ending = numbers[0]
    max_slice: List[int] = [numbers[0]]

    for number in numbers[1:]:
        max_ending = max(max_ending, number)
        max_slice.append(max_ending)
    return max_slice
