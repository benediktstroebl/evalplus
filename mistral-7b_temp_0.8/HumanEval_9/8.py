from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_element: int = numbers[0]
    rolling_max_elements: List[int] = []
    rolling_max_elements.append(max_element)

    for i in range(1, len(numbers)):
        new_max_element = max(max_element, numbers[i])
        rolling_max_elements.append(new_max_element)
        max_element = new_max_element

    return rolling_max_elements

