from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 1:
        return numbers
    result = []
    max_value = 0
    for index, number in enumerate(numbers):
        if number > max_value:
            max_value = number
        if index == len(numbers) - 1:
            result.append(max_value)
    return
