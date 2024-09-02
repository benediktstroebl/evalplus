from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 1
    return_list = [None] * (len(numbers) // window_size)
    for i in range(len(numbers)):
        window_start = i
        window_end = min(len(numbers), i + window_size + 1)
        max_value = max(numbers[window_start:window_end])
        return_list[window_start // window_size] = max_value
    return return_list[::-1]

