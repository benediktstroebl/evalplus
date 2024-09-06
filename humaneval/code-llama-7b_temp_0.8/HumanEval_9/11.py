from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_numbers: List[int] = []
    rolling_max_number = max(numbers)
    for number in numbers:
        rolling_max_number = max(number, rolling_max_number)
        max_numbers.append(rolling_max_number)

    return max_numbers

