from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # roll = 0
    # for i in range(len(numbers)):
    #     roll = max(numbers[i], roll)
    #     yield roll

    # or

    rolling_max = 0
    rolling_max_list = []
    for num in numbers:
        rolling_max = max(num, rolling_max)
        rolling_max_list.append(rolling_max)
    return rolling_max_list

