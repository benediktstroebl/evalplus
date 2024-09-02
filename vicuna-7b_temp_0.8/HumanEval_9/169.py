from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [0] * len(numbers)
    result = [None] * len(numbers)
    for i in range(len(numbers)):
        if i == 0:
            moments[i] = 1
        elif moments[i-1] + 1 == len(numbers):
            moments[i] = moments[i-1] + 1
        else:
            moments[i] = moments[i-1]
        result[i] = numbers[moments[i-1]:moments[i]]
    return result

