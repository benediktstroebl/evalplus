from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize local variables
    max_list = []
    max_val = 0

    for number in numbers:
        # if number is larger than current rolling maximum, update rolling maximum
        if number > max_val:
            max_val = number

        # append rolling maximum to list of rolling maximums
        max_list.append(max_val)

    return max_list

