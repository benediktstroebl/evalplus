from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 3
    running_max = [numbers[0]]
    for num in numbers[1:]:
        running_max.append(max(running_max[-window_size:]))
        running_max.insert(0, num)
    return running_max
