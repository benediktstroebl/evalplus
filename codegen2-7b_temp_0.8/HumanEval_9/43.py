from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_sum = numbers[0]
    res = [max_sum]
    for i, num in enumerate(numbers):
        if num > max_sum:
            max_sum = num
            res.append(num)
        else:
            res.append(max_sum)
    return res

