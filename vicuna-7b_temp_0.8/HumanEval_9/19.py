from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 0
    window = 0
    max_value = numbers[0]
    results = [max_value]

    for i in range(1, len(numbers)):
        if numbers[i] <= max_value:
            n += 1
            window = max_value
        else:
            window = max_value
            max_value = numbers[i]
            n = 1
            results = [max_value]

    return results[:n]

