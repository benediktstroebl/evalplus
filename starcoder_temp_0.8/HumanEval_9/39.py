from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = []
    for i, value in enumerate(numbers):
        if i == 0:
            results.append(value)
        else:
            results.append(max(value, results[i - 1]))
    return results

