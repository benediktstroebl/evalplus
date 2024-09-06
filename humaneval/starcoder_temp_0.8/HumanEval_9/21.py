from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elem = numbers[0]
    result = [max_elem]
    for elem in numbers[1:]:
        max_elem = max(elem, max_elem)
        result.append(max_elem)
    return result
