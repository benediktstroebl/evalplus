from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    res = []
    if len(numbers) == 1 or len(numbers) == 0:
        return res
    else:
        res.append(numbers[0])
        res.append(max(numbers[0], numbers[1]))
        for i in range(3, len(numbers) + 1):
            res.append(max(res[i - 1], res[i - 2]))
        return res

