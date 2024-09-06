from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_index = 0
    result = []

    for index, number in enumerate(numbers):
        if number > numbers[max_index]:
            max_index = index

        result.append(numbers[max_index])

    return result

