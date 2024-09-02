from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 1
    result = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result.append(max(numbers[i - n:i]))
        else:
            result.append(max(numbers[i - n:i + 1]))
        n += 1
    return result

