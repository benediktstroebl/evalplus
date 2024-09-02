from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    length = len(numbers)
    rolling_maxes = [numbers[0]]
    for i in range(1, length):
        max_index = 0
        max_value = numbers[0]
        for j in range(1, i):
            if numbers[j] > max_value:
                max_index = j
                max_value = numbers[j]
        rolling_maxes.insert(0, numbers[max_index])
    return rolling_maxes

