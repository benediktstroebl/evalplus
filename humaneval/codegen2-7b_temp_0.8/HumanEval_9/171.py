from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    start = 0
    end = 0
    max_number = numbers[start]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
            end = i
        else:
            end = end + 1
    return numbers[start:end] + [max_number]
