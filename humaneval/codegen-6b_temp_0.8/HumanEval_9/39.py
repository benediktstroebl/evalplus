from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_current = max(numbers)
    new_list = [max_current]
    for i in range(len(numbers) - 1):
        current = max_current
        max_current = max(max_current, numbers[i] + numbers[i + 1])
        new_list.append(max_current)
    return new_list

