from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number = None
    max_list = []
    for number in numbers:
        if max_number is None or max_number < number:
            max_number = number

        max_list.append(max_number)
    return max_list

