from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max = numbers[0]
    max_num = previous_max
    for num in numbers[1:]:
        if num > previous_max:
            previous_max = num
        elif num < previous_max:
            previous_max = num
        else:
            previous_max = num
        max_num = previous_max

    return [previous_max, max_num
