from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    start = 0
    max_value = numbers[0]
    current_numbers = numbers
    while current_numbers:
        if current_numbers[0] > max_value:
            max_value = current_numbers[0]
        current_numbers = current_numbers[1:]
        start += 1
    return [max_value] + max_value_sequence(current_numbers, start)

