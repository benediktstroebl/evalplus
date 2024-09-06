from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    length = len(numbers)
    result = [None] * length
    level = 0
    max_level = 0
    max_element = None

    while level < length:
        if numbers[level] > max_element:
            max_element = numbers[level]
            max_level = level
        if level == 0:
            result[level] = max_element
        else:
            result[level] = max_element
        level += 1

    for i in range(max_level + 1, length):
        if numbers[i] > result[i - 1]:
            result[i] = numbers[i]
        else:
            result[i] = result[i - 1]

    return result

