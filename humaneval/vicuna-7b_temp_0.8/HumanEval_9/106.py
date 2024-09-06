from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    max_numbers = [current_max]
    for i in range(1, len(numbers)):
        next_max = max(numbers[i:])
        max_numbers.append(next_max)
        numbers.remove(next_max)
        current_max = max(current_max, next_max)
    return max_numbers

