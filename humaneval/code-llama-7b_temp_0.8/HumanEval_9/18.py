from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Numbers must not be empty.")

    max_so_far = max(numbers)
    result = [max_so_far] * len(numbers)

    for i in range(1, len(numbers)):
        max_so_far = max(numbers[i], max_so_far - 1)
        result[i] = max_so_far
    return result

