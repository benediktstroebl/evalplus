from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # O(n), n - number of elements in the input list
    # prev_max is the list of max values for given moment
    prev_max: List[int] = [numbers[0]] * len(numbers)
    for i in range(1, len(numbers)):
        prev_max[i] = max(prev_max[i - 1], numbers[i])
    return prev_max

