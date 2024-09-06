from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return_array = [numbers[0]]
    for current_element in numbers[1:]:
        if current_element > return_array[-1]:
            return_array.append(current_element)
        else:
            return_array.append(return_array[-1])
    return return_array

