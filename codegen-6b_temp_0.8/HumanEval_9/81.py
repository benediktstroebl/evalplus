from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    max_values = [0] * n
    max_values[0] = numbers[0]
    for i in range(1, n):
        if numbers[i] > max_values[i - 1]:
            max_values[i] = numbers[i]
        else:
            max_values[i] = max_values[i - 1]
    result = [0] * n
    result[n - 1] = max_values[n - 1]
    for i in range(n - 2, 0, -1):
        if max_values[i - 1] < max_values[i]:
            result[i] = max_values[i]
        else:
            result[i] = result[i + 1]
    return result

