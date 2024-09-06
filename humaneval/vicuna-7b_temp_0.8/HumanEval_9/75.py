from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    result = []
    i = 0
    while i < n:
        max_index = i
        max_value = numbers[i]
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j
                max_value = numbers[j]
        result.append(max_value)
        i = max_index + 1
    return result

