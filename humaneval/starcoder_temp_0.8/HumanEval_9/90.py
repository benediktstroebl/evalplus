from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Empty list not allowed")

    # we start rolling maximum calculation from the 2nd element to the end
    # as rolling_max[0] is always equal to 1st element
    # rolling_max[i] is the maximum element in a subarray of length i
    # rolling_max[i] = max(rolling_max[i - 1], numbers[i])
    rolling_max: List[int] = [1] * len(numbers)
    for i in range(1, len(numbers)):
        if numbers[rolling_max[i - 1] - 1] >= numbers[i]:
            rolling_max[i] = rolling_max[i - 1]
        else:
            rolling_max[i] = i + 1
    return rolling_max

