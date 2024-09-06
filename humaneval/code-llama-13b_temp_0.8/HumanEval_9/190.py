from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        raise ValueError("Input array cannot be empty.")

    rolling_max_numbers = [numbers[0]]

    for number in numbers[1:]:
        if number > rolling_max_numbers[-1]:
            rolling_max_numbers.append(number)
        else:
            rolling_max_numbers.append(rolling_max_numbers[-1])
    return rolling_max_numbers

