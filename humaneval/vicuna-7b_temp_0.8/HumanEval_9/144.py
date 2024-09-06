from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = [None] * 10  # initialize a list of 10 None values
    length = len(numbers)  # get the length of the input list
    current_index = 0  # initialize the current index in the input list
    while current_index < length:  # start the loop from the first index
        if rolling_max[current_index] is None or numbers[current_index] > rolling_max[current_index]:  # if the rolling maximum is None or the current element is greater
            rolling_max[current_index] = numbers[current_index]
        current_index += 1

    return rolling_max[:current_index]  # return the rolling maximum elements found until current index
