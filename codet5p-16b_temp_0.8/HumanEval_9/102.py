from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    roll_max_list: List[int] = []
    temp_max: int = -1
    for i in range(len(numbers)):
        temp_max = max(numbers[i], temp_max)
        roll_max_list.append(temp_max)
    return roll_max_list

