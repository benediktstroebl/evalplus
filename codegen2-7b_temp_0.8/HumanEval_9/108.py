from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    values = []
    max_val = 0
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            values.append(max_val)
            max_val = numbers[i]
        else:
            max_val = max(max_val, numbers[i])
    values.append(max_val)
    return
