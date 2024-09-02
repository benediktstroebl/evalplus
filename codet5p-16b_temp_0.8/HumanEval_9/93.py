from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    for i in range(len(numbers)):
        max_val = numbers[i]
        for j in range(i, len(numbers)):
            max_val = max(max_val, numbers[j])
            result.append(max_val)
    return result

