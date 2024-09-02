from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    lst = []
    for idx, num in enumerate(numbers):
        if idx == 0:
            lst.append(num)
        else:
            lst.append(max(num, numbers[idx-1]))
    return lst

