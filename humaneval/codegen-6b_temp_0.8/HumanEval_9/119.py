from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max = None
    for i in range(1, len(numbers) + 1):
        if max is None:
            max = numbers[i - 1]
        elif max < numbers[i - 1]:
            max = numbers[i - 1]
        result.append(max)
    return result

