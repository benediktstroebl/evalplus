from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_numbers = []

    # max_number starts at the minimum integer possible
    max_number = min(numbers)

    for i, number in enumerate(numbers):
        if number > max_number:
            max_number = number

        rolling_max_numbers.append(max_number)

    return rolling_max_numbers

