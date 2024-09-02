from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    current_max = 0
    for i in range(len(numbers) - 1):
        current_num = numbers[i]
        max_list.append(current_max)
        current_max = current_num
    max_list.append(current_max)
    return max_list

