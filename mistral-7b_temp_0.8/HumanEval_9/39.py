from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_element = 0
    max_elements = []
    for num in numbers:
        last_element = max(num, last_element)
        max_elements.append(last_element)
    return max_elements

