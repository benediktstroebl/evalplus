from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_elements = []
    max_element = None
    for i in numbers:
        if max_element is None or i > max_element:
            max_element = i
        rolling_max_elements.append(max_element)
    return rolling_max_elements

