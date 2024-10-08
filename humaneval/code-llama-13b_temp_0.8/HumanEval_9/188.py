from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_element = 0
    rolling_max_list = []
    for number in numbers:
        rolling_max_element = max(rolling_max_element, number)
        rolling_max_list.append(rolling_max_element)

    return rolling_max_list

