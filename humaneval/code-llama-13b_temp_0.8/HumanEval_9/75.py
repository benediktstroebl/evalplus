from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_values = [numbers[0]]
    max_value = numbers[0]

    for value in numbers[1:]:
        max_value = max(value, max_value)
        rolling_max_values.append(max_value)

    return rolling_max_values

