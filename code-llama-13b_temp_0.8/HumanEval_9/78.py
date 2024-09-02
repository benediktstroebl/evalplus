from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_value = numbers[0]
    rolling_max_list: List[int] = [rolling_max_value]
    for number in numbers[1:]:
        if number >= rolling_max_value:
            rolling_max_value = number
        rolling_max_list.append(rolling_max_value)
    return rolling_max_list

