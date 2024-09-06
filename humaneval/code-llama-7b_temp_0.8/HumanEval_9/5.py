from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = numbers[0]
    rolling_max = [max_val]
    for number in numbers[1:]:
        max_val = max(number, max_val)
        rolling_max.append(max_val)
    return rolling_max

