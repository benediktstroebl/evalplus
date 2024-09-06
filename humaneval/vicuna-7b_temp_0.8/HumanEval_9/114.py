from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 1
    max_nums = []
    for num in numbers:
        if n == len(numbers):
            max_nums.append(max(max_nums))
        else:
            max_nums.append(max(max_nums[-1:]))
            max_nums.append(num)
            n += 1
    return max_nums

