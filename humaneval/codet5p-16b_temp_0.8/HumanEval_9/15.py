from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_list: List[int] = []
    max_at_moment: int = numbers[0]
    rolling_max_list.append(max_at_moment)

    for index in range(1, len(numbers)):
        max_at_moment = max(numbers[index], max_at_moment)
        rolling_max_list.append(max_at_moment)

    return rolling_max_list

