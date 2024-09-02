from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_values = []
    for start, end in enumerate(numbers[:-1]):
        max_values.append(max(numbers[start:end+1]))
    max_values.append(numbers[-1])
    return max_values

