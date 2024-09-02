from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_elem = numbers[0]
    for num in numbers:
        if num > max_elem:
            max_elem = num
        else:
            result.append(max_elem)
    return
