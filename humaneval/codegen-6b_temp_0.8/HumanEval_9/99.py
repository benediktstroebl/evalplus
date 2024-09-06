from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = max(numbers)
    new_numbers = [max_num] * len(numbers)
    for i in range(len(numbers)):
        if i > 0:
            new_numbers[i] = max(new_numbers[i - 1], numbers[i])
    return new_numbers

