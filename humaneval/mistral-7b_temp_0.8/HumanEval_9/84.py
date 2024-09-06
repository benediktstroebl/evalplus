from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Cannot find maximum element in empty sequence.")

    max_value = numbers[0]
    rolling_max = [max_value]

    for element in numbers[1:]:
        if element > max_value:
            max_value = element
        rolling_max.append(max_value)

    return rolling_max

