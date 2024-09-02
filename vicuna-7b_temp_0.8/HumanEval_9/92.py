from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    size = len(numbers)
    max_found = [numbers[0]]
    for i in range(1, size):
        for j in range(i - 1, size - 1, -1 if numbers[i] > numbers[j] else 1):
            max_found.append(max(numbers[i:j+1]))
    return max_found