from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # The output list to be returned
    rolling_max_list = []
    # Iterate through the input list
    for i, num in enumerate(numbers):
        # If i is zero, the output list is equal to the input list
        if i == 0:
            rolling_max_list = numbers
        # Otherwise, if the current number is bigger than the rolling maximum, the rolling maximum
        # becomes the current number
        elif num > rolling_max_list[i - 1]:
            rolling_max_list[i - 1] = num
    return rolling_max_list

