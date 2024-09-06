from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_values: List[int] = []
    rolling_max_value = max(numbers)
    rolling_max_values.append(rolling_max_value)

    for index in range(len(numbers) - 1):
        current_value = numbers[index]
        next_value = numbers[index + 1]
        if current_value > next_value:
            rolling_max_value = current_value
        else:
            rolling_max_value = max(rolling_max_value, next_value)
        rolling_max_values.append(rolling_max_value)
    return rolling_max_values

