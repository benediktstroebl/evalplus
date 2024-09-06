from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    length = len(numbers)
    result = []
    for i in range(length):
        max_found = numbers[i]
        for j in range(i + 1, length):
            numbers[j] = numbers[j - 1]
        numbers[i] = max_found
        result.append(max_found)
    return result

