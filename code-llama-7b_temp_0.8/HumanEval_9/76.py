from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val: int = max(numbers)
    rolling_max_list: List[int] = [max_val]
    for i in numbers:
        max_val = max_val if i <= max_val else i
        rolling_max_list.append(max_val)
    return rolling_max_list

