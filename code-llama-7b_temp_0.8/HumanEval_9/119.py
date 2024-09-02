from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Cannot process empty list")

    rolling_max_numbers: List[int] = []

    rolling_max_numbers.append(max(numbers))

    for index in range(1, len(numbers)):
        if numbers[index] > rolling_max_numbers[-1]:
            rolling_max_numbers.append(numbers[index])
        else:
            rolling_max_numbers.append(rolling_max_numbers[-1])

    return rolling_max_numbers

