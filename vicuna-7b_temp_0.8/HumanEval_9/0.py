from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = numbers[0]
    window_size = 1
    return_list = []
    for i in range(1, len(numbers)):
        for j in range(window_size):
            if numbers[i - j] >= max_val:
                max_val = numbers[i - j]
        return_list.append(max_val)
        max_val = numbers[i]
        window_size += 1

    return return_list

