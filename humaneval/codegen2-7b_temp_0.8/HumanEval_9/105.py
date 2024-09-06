from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max = 0
    max_list = []
    for i in range(0, len(numbers)):
        if numbers[i] > max:
            max_list.append(max)
            max = numbers[i]
        else:
            max = max if max >= numbers[i] else numbers[i]
    max_list.append(max)
    return max_
