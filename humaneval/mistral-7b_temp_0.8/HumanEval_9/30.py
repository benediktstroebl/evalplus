from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = numbers[0]
    max_indices = [0]

    for i in range(1, len(numbers)):
        value = numbers[i]
        if value >= max_value:
            max_value = value
            max_indices.append(i)

    return max_indices

