from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_element = []
    max_element.append(numbers[0])
    for index, number in enumerate(numbers[1:], 1):
        max_element.append(max(number, max_element[index - 1]))
    return max_element

