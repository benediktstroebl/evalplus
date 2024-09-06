from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elem = numbers[0]
    current_max = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > current_max:
            current_max = numbers[index]
        else:
            current_max = max(current_max, numbers[index])
    return [max_elem, current_max
