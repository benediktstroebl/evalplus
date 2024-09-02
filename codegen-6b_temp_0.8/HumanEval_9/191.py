from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    if len(numbers) <= 1:
        return numbers
    max_found = numbers[0]
    result.append(max_found)
    for i in range(1, len(numbers)):
        max_found = max(max_found, numbers[i])
        result.append(max_found)
    return result

