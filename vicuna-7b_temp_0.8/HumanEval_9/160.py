from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_max = max(numbers)
    result = [last_max]
    current = last_max
    for n in range(len(numbers) - 1):
        if numbers[n] > current:
            current = numbers[n]
        result.append(current)
    return result

