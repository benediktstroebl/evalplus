from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = [None] * len(numbers)
    for i in range(len(numbers)):
        result[i] = numbers[i]
        for j in range(i, max(0, i - len(numbers)), -1):
            if numbers[j] > result[i]:
                result[i] = numbers[j]
                break
    return result

