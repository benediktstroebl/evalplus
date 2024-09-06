from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [None] + numbers  # Add None into numbers so that the index is valid.
    result = [None,] * (len(numbers) - 1)
    for idx in range(len(numbers) - 1):
        if idx == 0:
            result[idx] = max(numbers[1], numbers[2])
        else:
            result[idx] = max(numbers[idx + 1], result[idx - 1])
    return result

