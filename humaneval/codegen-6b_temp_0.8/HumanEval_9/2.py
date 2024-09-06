from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    indexes, max_elements = [], []
    for index, element in enumerate(numbers):
        indexes.append(index)
        if index == 0:
            max_elements.append(element)
        elif element > max_elements[-1]:
            max_elements.append(element)
        else:
            max_elements.append(max_elements[-1])

    while len(max_elements) < len(numbers):
        max_elements.append(max_elements[-1])

    return max_elements

