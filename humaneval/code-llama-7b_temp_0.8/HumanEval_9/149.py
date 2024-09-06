from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_numbers = [None] * len(numbers)
    for i, number in enumerate(numbers):
        if i == 0:
            rolling_max_numbers[i] = number
        else:
            previous_number = rolling_max_numbers[i - 1]
            rolling_max_numbers[i] = max(previous_number, number)
    return rolling_max_numbers

