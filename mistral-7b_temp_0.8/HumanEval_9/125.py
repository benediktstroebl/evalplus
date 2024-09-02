from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_so_far = []
    max_element = numbers[0]
    rolling_max_so_far.append(max_element)
    for i in range(1, len(numbers)):
        element = numbers[i]
        if element > max_element:
            max_element = element
        rolling_max_so_far.append(max_element)
    return rolling_max_so_far

