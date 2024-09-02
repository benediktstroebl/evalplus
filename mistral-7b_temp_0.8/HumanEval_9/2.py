from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number = 0
    new_list = []
    for i, number in enumerate(numbers):
        if number > max_number:
            new_list.append(number)
            max_number = number
        else:
            new_list.append(max_number)
    return new_list

