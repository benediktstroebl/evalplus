from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = numbers[:]
    max_num = max(numbers)
    max_idx = len(numbers) - 1
    result = []
    for _ in range(len(numbers)):
        result.append(max_num)
        numbers[max_idx] = max(numbers[max_idx - 1], max_num)
        max_num = max(numbers[max_idx - 1], max_num)
        max_idx = max_idx - 1
    return result

