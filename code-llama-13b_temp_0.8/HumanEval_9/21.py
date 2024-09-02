from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    previous_max = max(numbers[0], numbers[1])
    rolling_max_list = [previous_max]
    for index in range(2, len(numbers)):
        max_value = max(previous_max, numbers[index])
        rolling_max_list.append(max_value)
        previous_max = max_value
    return rolling_max_list

