from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    rolling_max = numbers[0]
    max_list = [rolling_max]
    for num in numbers[1:]:
        rolling_max = max(num, rolling_max)
        max_list.append(rolling_max)
    return max_list

