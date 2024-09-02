from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [0]
    result = [0]
    for i in range(len(numbers) + 1):
        curr_moment = moments[i - 1]
        curr_max = max(numbers[curr_moment - 1:])
        if curr_max > result[-1]:
            result[-1] = curr_max
        else:
            result.append(curr_max)
        moments.append(i)
    return result