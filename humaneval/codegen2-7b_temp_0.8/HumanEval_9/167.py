from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_values = [0] * len(numbers)
    for i, value in enumerate(numbers):
        if value > max_values[i]:
            max_values[i] = value
        if i < len(numbers) - 1 and max_values[i] < numbers[i + 1]:
            max_values[i + 1] = max(value, max_values[i + 1])
    return max_
