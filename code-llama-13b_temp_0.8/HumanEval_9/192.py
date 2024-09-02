from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    index = 0
    max_value = numbers[0]
    result = []
    while index < len(numbers):
        element = numbers[index]
        if max_value < element:
            max_value = element
        result.append(max_value)
        index += 1
    return result

