from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    number_of_rolling = 3
    rolling = []
    for i in range(len(numbers)):
        rolling_max_element = numbers[i]
        rolling.append(rolling_max_element)
        if len(rolling) == number_of_rolling:
            return rolling[:number_of_rolling]
    return []

