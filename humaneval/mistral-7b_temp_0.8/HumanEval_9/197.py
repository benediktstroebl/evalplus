from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = [0]
    if len(numbers) == 1:
        return numbers
    for index, number in enumerate(numbers):
        rolling_max_list.append(max(rolling_max_list[-1], number))
        rolling_max_list.pop(0)
    return rolling_max_list

