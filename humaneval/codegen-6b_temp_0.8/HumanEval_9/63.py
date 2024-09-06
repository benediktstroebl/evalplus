from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = [numbers[0]]
    for n in numbers:
        if n > results[-1]:
            results.append(n)
        else:
            results.append(results[-1])
    return results

