from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = list()
    maximum_num = -1
    for num in numbers:
        if num >= maximum_num:
            maximum_num = num
        result.append(maximum_num)
    return result

