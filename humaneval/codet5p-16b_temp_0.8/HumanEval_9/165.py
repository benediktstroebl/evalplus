from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Initialize
    result = []
    max_n = numbers[0]
    for index, n in enumerate(numbers):
        if n > max_n:
            max_n = n
        result.append(max_n)
    return result

