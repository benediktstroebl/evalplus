from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous = numbers[0]
    window = [numbers[0]]
    for value in numbers[1:]:
        if value > previous:
            window.append(value)
            previous = value
        else:
            previous = max(previous, value)
    window.append(previous)
    return window

