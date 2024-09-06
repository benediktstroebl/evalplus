from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_numbers = []
    for current_index, current_number in enumerate(numbers):
        maximum = current_number
        for previous_index in range(current_index):
            maximum = max(maximum, numbers[previous_index])
        rolling_max_numbers.append(maximum)
    return rolling_max_numbers

