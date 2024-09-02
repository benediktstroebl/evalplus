from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return numbers

    max_num = numbers[0]
    for i, num in enumerate(numbers):
        if num > max_num:
            max_num = num
        numbers[i] = max_num
    return numbers

