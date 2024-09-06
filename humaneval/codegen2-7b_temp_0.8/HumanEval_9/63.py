from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_maximum = numbers[0]
    current_maximum = previous_maximum

    for number in numbers[1:]:
        current_maximum = max(number, current_maximum + 1)
        previous_maximum = current_maximum

    return [current_maximum] + [previous_maximum] * (len(numbers) - 1
