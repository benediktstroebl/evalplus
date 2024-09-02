from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    start_idx = 0
    while start_idx < len(numbers):
        max_n = numbers[start_idx]
        idx = start_idx + 1

        while idx < len(numbers):
            if numbers[idx] > max_n:
                max_n = numbers[idx]
            idx += 1
        result.append(max_n)
        start_idx += 1
    return result

