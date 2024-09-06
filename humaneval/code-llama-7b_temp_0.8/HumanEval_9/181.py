from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        raise IndexError('List should have at least one element.')
    max_so_far = numbers[0]
    rolling_maxes = [numbers[0]]
    for number in numbers[1:]:
        if number > max_so_far:
            max_so_far = number
        rolling_maxes.append(max_so_far)
    return rolling_maxes

