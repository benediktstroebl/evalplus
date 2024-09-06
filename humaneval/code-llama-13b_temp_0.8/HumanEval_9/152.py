from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_index: int = 0
    rolling_max_values: List[int] = []

    for index, number in enumerate(numbers):
        if numbers[rolling_max_index] < number:
            rolling_max_index = index
        rolling_max_values.append(numbers[rolling_max_index])

    return rolling_max_values

