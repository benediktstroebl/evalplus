from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [None for _ in numbers]
    result[0] = numbers[0]

    for idx in range(1, len(numbers)):
        result[idx] = max(result[idx - 1], numbers[idx])

    return result

