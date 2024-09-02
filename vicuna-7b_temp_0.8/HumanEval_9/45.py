from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index

    return numbers[max_index:]

