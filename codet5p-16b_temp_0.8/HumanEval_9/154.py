from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    for i in range(len(numbers)):
        rolling_max_until_i = [numbers[j] for j in range(i, len(numbers)) if numbers[j] > numbers[i]]
        result.append(max(rolling_max_until_i) if rolling_max_until_i else numbers[i])
    return result

