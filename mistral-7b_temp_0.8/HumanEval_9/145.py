from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = 0
    result = []
    for number in numbers:
        if number > max_num:
            result.append(number)
            max_num = number
        else:
            result.append(max_num)
    return result

