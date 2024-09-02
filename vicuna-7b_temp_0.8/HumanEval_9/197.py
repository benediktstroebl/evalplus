from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    max_value = max(numbers)
    current_max_value = max_value
    current_max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > current_max_value:
            current_max_index = i - 1
            current_max_value = numbers[i]
        elif numbers[i] == current_max_value:
            current_max_index += 1
        else:
            current_max_index = i

        numbers[current_max_index] = max_value
        max_index = current_max_index
        max_value = current_max_value

    return numbers[:max_index + 1]

