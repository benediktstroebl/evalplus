from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    max_index = 0
    for index, element in enumerate(numbers):
        if element > numbers[max_index]:
            max_index = index
        result.append(numbers[max_index])
    return result

