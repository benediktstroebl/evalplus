from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = max(numbers)
    max_index = numbers.index(max_value)
    rolling_max = [max_value]
    for i in range(max_index + 1):
        rolling_max.append(numbers[i])
        numbers.pop(i)
    return rolling_max

