from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize empty list of rolling maxima
    rolling_max_list = []
    current_max = numbers[0]

    for num in numbers:
        # if the current number is greater than the current maximum, update the maximum and append to rolling_max_list
        if num > current_max:
            current_max = num
            rolling_max_list.append(current_max)
        else:
            # otherwise, append the current number to the rolling_max_list
            rolling_max_list.append(current_max)

        # update the current maximum with the current number
        current_max = num

    return rolling_max_list

