from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_to_cur_index = [0 for _ in range(len(numbers))]
    max_to_cur_index[0] = numbers[0]
    for index in range(1, len(numbers)):
        max_to_cur_index[index] = max(max_to_cur_index[index-1], numbers[index])

    return max_to_cur_index

