from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    max_value = numbers[max_index]
    for i in range(len(numbers)):
        if max_value < numbers[i]:
            max_value = numbers[i]
            max_index = i
    return [max_value] + numbers[max_index:]

