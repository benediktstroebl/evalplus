from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [None] * len(numbers)
    result[0] = numbers[0]
    max_val_to_right = numbers[0]
    for idx in range(1, len(numbers)):
        if numbers[idx] > max_val_to_right:
            result[idx] = numbers[idx]
        else:
            result[idx] = max_val_to_right
        max_val_to_right = max(max_val_to_right, numbers[idx])
    return result

