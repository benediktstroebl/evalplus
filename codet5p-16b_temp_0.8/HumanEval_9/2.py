from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_list = []
    rolling_max_list = []
    rolling_max_list.append(numbers[0])
    for i in range(1, len(numbers)):
        max_list.append(numbers[i] if numbers[i] > numbers[i - 1] else numbers[i - 1])
        rolling_max_list.append(max_list[i - 1] if max_list[i - 1] > numbers[i] else numbers[i])
    return rolling_max_list

