from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = numbers[0]
    window = [numbers[0]]
    for i in range(1, len(numbers)):
        window.append(numbers[i] if max_val < numbers[i] else max_val)
        if max_val < numbers[i]:
            max_val = numbers[i]
    return window

