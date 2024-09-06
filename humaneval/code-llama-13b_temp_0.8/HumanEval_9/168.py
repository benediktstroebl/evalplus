from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # store the maximum integer found until given moment
    maximum = -float("inf")
    rolling_max = []

    for i in numbers:
        # if new value is bigger than the maximum, update the maximum value
        if maximum < i:
            maximum = i

        rolling_max.append(maximum)
    return rolling_max

