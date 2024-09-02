from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Numbers cannot be empty.")
    max_number = max(numbers)
    result = [max_number] * len(numbers)

    for i in range(len(numbers)):
        if numbers[i] < max_number:
            result[i] = max_number
        else:
            max_number = numbers[i]

    return result

