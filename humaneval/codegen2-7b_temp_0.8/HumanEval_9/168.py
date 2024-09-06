from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []

    first_max = numbers[0]
    new_max = first_max
    for number in numbers[1:]:
        if number > new_max:
            new_max = number

    return [first_max] + rolling_max(numbers[1:])

