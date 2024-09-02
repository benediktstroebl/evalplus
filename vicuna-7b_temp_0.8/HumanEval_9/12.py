from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 0
    max_val = numbers[0]
    max_number = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
            max_number = num
        n += 1
    return [max_val, max_number]

