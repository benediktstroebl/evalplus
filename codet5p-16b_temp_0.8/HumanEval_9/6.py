from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_list: List[int] = []
    while len(numbers) > 0:
        current_max: int = max(numbers)
        rolling_max_list.append(current_max)
        numbers.pop(numbers.index(current_max))
    return rolling_max_list

