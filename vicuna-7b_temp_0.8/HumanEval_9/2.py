from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    length = len(numbers)
    result = numbers[:length]
    for i in range(1, length):
        max_index = result.index(max(result))
        result.remove(numbers[max_index])
        result.insert(i, numbers[max_index])
    return result

