from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 1:
        return [numbers[0]]
    left = numbers[0]
    right = numbers[1]
    rolling_max = [left if left > right else right]
    for i in range(2, len(numbers)):
        next_num = numbers[i]
        if left > right:
            rolling_max.append(left if left > next_num else next_num)
        else:
            rolling_max.append(right if right > next_num else next_num)
    return rolling_max

