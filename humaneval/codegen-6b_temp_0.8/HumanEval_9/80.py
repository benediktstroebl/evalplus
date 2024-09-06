from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    max_so_far_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
            max_so_far_list = [numbers[i]]
        else:
            max_so_far_list.append(numbers[i])
    return max_so_far_list

