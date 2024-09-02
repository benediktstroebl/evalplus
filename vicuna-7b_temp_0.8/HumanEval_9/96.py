from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers_rev = sorted(numbers[1:], reverse=True)
    while len(numbers_rev) > 0:
        max_value = max(numbers_rev)
        numbers_rev.remove(max_value)
        numbers.insert(0, max_value)
    return numbers

