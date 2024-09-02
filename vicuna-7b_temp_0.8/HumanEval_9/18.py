from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_max_value = numbers[-1]
    max_values = [last_max_value]

    for current_value in numbers[1:]:
        max_values.append(max(max_values) if max_values else current_value)

    return max_values[-1]

