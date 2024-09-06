from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_element = numbers[0]
    rolling_max_list = [max_element]

    for current_element in numbers[1:]:
        max_element = max(max_element, current_element)
        rolling_max_list.append(max_element)

    return rolling_max_list

