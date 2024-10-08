from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    start = 0
    max_values = [max(numbers[i:]) for i in range(len(numbers) + 1)]
    return [max_values[j] for j in range(len(start) + len(max_values) - len(numbers))]

