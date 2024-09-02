from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 0
    result = []
    current_max = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] <= current_max:
            n += 1
            result.append(current_max)
            current_max = max(numbers[i+1:])
        else:
            result.append(max(result) if n == 0 else max(result[n-1:]) + 1)
            n = 0
    result.append(max(result) if n == 0 else max(result[n-1:]) + 1)
    return result

