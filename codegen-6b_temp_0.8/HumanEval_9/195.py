from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    index, count = 0, 0
    for i in range(len(numbers)):
        count = 1 if numbers[i] > numbers[index] else 0
        index = i if numbers[i] > numbers[index] else index
        result.append(numbers[index])
    return result

