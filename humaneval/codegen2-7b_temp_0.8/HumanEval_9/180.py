from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elem = numbers[0]
    for num in numbers[1:]:
        if num > max_elem:
            max_elem = num
        else:
            max_elem = max(max_elem, num)
    return [max_elem] + rolling_max(numbers[1:])

