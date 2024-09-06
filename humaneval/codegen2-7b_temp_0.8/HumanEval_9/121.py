from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_ = -999999
    rolling = []
    for index, element in enumerate(numbers):
        if element > max_:
            rolling = [element]
            max_ = element
        elif element == max_:
            rolling.append(element)
        else:
            rolling.pop()
            rolling.append(element)

    return rolling

