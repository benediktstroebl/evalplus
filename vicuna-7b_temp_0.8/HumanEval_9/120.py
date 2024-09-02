from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize a list to store the rolling maximum values
    rolling_max_list = []
    # keep track of the last maximum value encountered
    last_max = numbers[0]
    # iterate through the numbers
    for num in numbers[1:]:
        # if the current number is greater than the last maximum, reset the rolling maximum list
        if num > last_max:
            rolling_max_list = [num]
        # add the current number to the rolling maximum list
        rolling_max_list.append(num)
        # update the last maximum value
        last_max = max(rolling_max_list[-1], num)
    # add the last maximum value to the rolling maximum list
    rolling_max_list.append(last_max)
    return rolling_max_list

