from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    max_element = numbers[0]
    for number in numbers[1:]:
        if number > max_element:
            max_element = number
        rolling_max.append(max_element)
    return rolling_max

