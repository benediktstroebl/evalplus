from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize the rolling max and the index
    rolling_max = numbers[0]
    index = 0

    # iterate through the numbers
    for num in numbers[1:]:
        # update the rolling max and the index
        rolling_max = max(rolling_max, num)
        index += 1

    return [rolling_max, index]