from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Define an empty list to contain the rolling max elements
    rolling_max = [0] * len(numbers)
    rolling_max[0] = numbers[0]

    # Iterate over the list of numbers
    for index in range(1, len(numbers)):
        rolling_max[index] = max(rolling_max[index - 1], numbers[index])

    return rolling_max

