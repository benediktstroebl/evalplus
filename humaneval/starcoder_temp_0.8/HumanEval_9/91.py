from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = [numbers[0]]

    for current_index, current_value in enumerate(numbers[1:]):
        previous_index = current_index + 1
        if current_value > max_list[previous_index]:
            max_list.append(current_value)
        else:
            max_list.append(max_list[previous_index])

    return max_list

