from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_number = numbers[0]
    rolling_max_numbers = [max_number]

    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            rolling_max_numbers.append(numbers[i])
            max_number = numbers[i]
        else:
            rolling_max_numbers.append(max_number)

    return rolling_max_numbers

