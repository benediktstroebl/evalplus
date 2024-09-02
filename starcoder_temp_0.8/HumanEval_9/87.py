from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    rolling_max_nums = [numbers[0]]
    for num in numbers:
        if num > rolling_max_nums[-1]:
            rolling_max_nums.append(num)
        else:
            rolling_max_nums.append(rolling_max_nums[-1])
    return rolling_max_nums

