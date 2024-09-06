from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_until_index = 0
    max_until_list = []
    for index in range(len(numbers)):
        max_until_list.append(max(numbers[max_until_index:index+1]))
        max_until_index += 1 if numbers[index] == max_until_list[-1] else 0
    return max_until_list

