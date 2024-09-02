from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    def rolling_max_aux(index, maxes):
        if index >= len(numbers):
            return maxes

        max_num = max(numbers[index], *maxes)
        return rolling_max_aux(index + 1, [max_num])

    return rolling_max_aux(0, [])

