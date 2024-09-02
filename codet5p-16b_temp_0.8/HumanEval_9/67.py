from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    if not numbers:
        return result
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        result.append(max_num)
    return result

