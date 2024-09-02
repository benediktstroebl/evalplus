from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max = -float('inf')
    rolling_max_numbers = []
    for number in numbers:
        previous_max = max(number, previous_max)
        rolling_max_numbers.append(previous_max)
    return rolling_max_numbers

