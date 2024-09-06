from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 5  # maximum number of elements to consider
    result = []
    start = 0
    for i in range(1, len(numbers)):
        # find the maximum element from the start of the sequence up to the current element
        max_found = numbers[start:i]
        result.append(max(max_found))
        start = i
    # add the last element found
    result.append(numbers[start])
    return result

