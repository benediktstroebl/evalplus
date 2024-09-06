from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = max(numbers)
    current_index = len(numbers) - 1
    result = [max_value] * current_index
    while current_index > 0:
        current_max = max(numbers[:current_index + 1])
        if current_max > max_value:
            max_value = current_max
        result[current_index - 1] = max_value
        current_index -= 1
    return result

