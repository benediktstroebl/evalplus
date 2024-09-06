from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = [None] * len(numbers)
    results[0] = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > results[i - 1]:
            results[i] = numbers[i]
        else:
            results[i] = results[i - 1]
    return results

