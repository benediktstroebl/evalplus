from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [0] * 10
    result = [0] * len(numbers)
    for i in range(10):
        for j in range(len(numbers)):
            if j - moments[i] >= 0:
                result[j] = numbers[j - moments[i]]
        moments[i] += 1
    return result

