from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = max(numbers)
    index = 0
    result = [max_val]
    while len(result) < len(numbers):
        if numbers[index] > max_val:
            max_val = numbers[index]
            index = index + 1
        result.append(max_val)
    return result