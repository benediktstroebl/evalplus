from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    for i in numbers[1:]:
        if result[-1] < i:
            result.append(i)
        elif result[-1] == i:
            result.append(i)
        else:
            result[-1] = i
    return result

