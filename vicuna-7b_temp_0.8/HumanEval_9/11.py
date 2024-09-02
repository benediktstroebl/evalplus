from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    n = len(numbers)
    result = [numbers[0]]
    current_max = numbers[0]
    for i in range(1, n):
        for j in range(i):
            max_diff = abs(numbers[j] - numbers[i])
            if max_diff > current_max:
                current_max = max_diff
            result.append(current_max)
    return result[::-1]

