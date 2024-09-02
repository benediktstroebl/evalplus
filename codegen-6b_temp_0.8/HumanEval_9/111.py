from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    cur_max = numbers[0]
    max_list = [cur_max]
    for i in range(1, len(numbers)):
        if numbers[i] > cur_max:
            cur_max = numbers[i]
        else:
            cur_max = max(cur_max, numbers[i])
        max_list.append(cur_max)
    return max_list

