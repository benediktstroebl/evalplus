from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximum_found = numbers[0]
    maximums = [maximum_found]

    for element in numbers[1:]:
        maximum_found = max(element, maximum_found)
        maximums.append(maximum_found)

    return maximums

