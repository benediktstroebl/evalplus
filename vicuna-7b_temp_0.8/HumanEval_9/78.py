from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize rolling window to a single element
    window = numbers[0]
    max_window = numbers[0]
    current_max = numbers[0]
    for number in numbers[1:]:
        # add the current number to the rolling window
        window += number
        # update the maximum of the rolling window
        max_window = max(max_window, window)
        # update the current maximum
        current_max = max_window
    return current_max

