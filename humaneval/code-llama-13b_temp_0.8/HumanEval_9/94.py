from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # HINT: keep track of the rolling maximum and the rolling maximum index.
    #       the next maximum index will be the same as current if the current
    #       number is the same or higher than the previous maximum value
    rolling_max_list: List[int] = []
    rolling_max_value = numbers[0]
    rolling_max_index = 0
    for index, number in enumerate(numbers):
        if number > rolling_max_value:
            rolling_max_value = number
            rolling_max_index = index
        rolling_max_list.append(numbers[rolling_max_index])
    return rolling_max_list

