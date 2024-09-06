from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for i in range(len(numbers)):
        if i == 0:
            m = max(numbers[0], numbers[1])
            max_list.append(m)
        else:
            m = max(max_list[i - 1], numbers[i])
            max_list.append(m)
    return max_list

