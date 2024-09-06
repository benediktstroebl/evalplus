from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_max = numbers[0]
    maxs = [last_max]
    for number in numbers[1:]:
        if number > last_max:
            last_max = number
        else:
            last_max = max(last_max, number)
        maxs.append(last_max)
    return max
